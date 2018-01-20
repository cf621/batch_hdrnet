#!/usr/bin/env python
# Feng Chen <achenfengb@gmail.com>
#
# batch version of hdrnet training fuction. You just need to put all the tasks to corresponding folder. That's it. You are done.
#

import os
import logging
import argparse

logging.basicConfig(format="[%(process)d] %(levelname)s %(filename)s:%(lineno)s | %(message)s")
log = logging.getLogger("batch training")
log.setLevel(logging.INFO)

if __name__ == "__main__":
    #required arguements
    parser = argparse.ArgumentParser()
    parser.add_argument('checkpoint_dir', default=None, help='direct to save checkpoints to.')
    parser.add_argument('data_dir', default=None, help='input directory containing all training tasks\'s .tfrecords or images.')
    #optional argument
    parser.add_argument('--eval_data_dir', default=None, type=str, help='directory with the validation data.')
    parser.add_argument('--rest', default=None, type=str, help='the rest of optional paramters for hdrnet.')

    args = parser.parse_args()

    log.info('Start training...')
    log.info('The checkpoint dir ' + args.checkpoint_dir)
    log.info('The data folder ' + args.data_dir)

    task_dirs = [ o for o in os.listdir(args.data_dir) if os.path.isdir(os.path.join(args.data_dir, o)) and not o.startswith('.') ]
    task_cmd0 = os.path.join(os.path.dirname(os.path.realpath(__file__)),'train.py ')
    os.system('rm -rf ' + os.path.join(args.checkpoint_dir, '*'))

    for task in task_dirs:
        log.info('*****************Begin task {}*************************'.format(task))
        checkpoint_dir = os.path.join(args.checkpoint_dir, task)
        data_dir = os.path.join(args.data_dir, task, 'filelist.txt')

        os.mkdir(checkpoint_dir)

        task_cmd = task_cmd0 + checkpoint_dir + ' ' + data_dir

        if  args.eval_data_dir:
            eval_data_dir = os.path.join(args.eval_data_dir, task)
            task_cmd += ' --eval_data_dir ' + eval_data_dir
            
        if args.rest:
            task_cmd += ' ' + args.rest

        print task_cmd
        os.system(task_cmd)
        log.info('\n****************End task {}*************************\n'.format(task))
