#!/usr/bin/env python
# Feng Chen <achenfengb@gmail.com>
#
# batch version of hdrnet freeze_graphy.py. You just need to put all the tasks to corresponding folder. That's it. You are done.
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
    parser.add_argument('checkpoint_dir', default=None, help='path to the batch of saved model variables')

    #optional argument
    parser.add_argument('--rest', default=None, type=str, help='the rest of optional paramters for hdrnet.')

    args = parser.parse_args()

    log.info('Start freezing graph...')
    log.info('The checkpoint dir ' + args.checkpoint_dir)

    task_dirs = [ o for o in os.listdir(args.checkpoint_dir) if os.path.isdir(os.path.join(args.checkpoint_dir, o)) and not o.startswith('.') ]
    task_cmd0 = os.path.join(os.path.dirname(os.path.realpath(__file__)),'freeze_graph.py ')

    for task in task_dirs:
        log.info('*****************Begin task {}*************************'.format(task))
        checkpoint_dir = os.path.join(args.checkpoint_dir, task)

        task_cmd = task_cmd0 + checkpoint_dir

        if args.rest:
            task_cmd += ' ' + args.rest

        os.system(task_cmd)
        log.info('\n****************End task {}*************************\n'.format(task))
