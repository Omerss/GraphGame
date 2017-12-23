#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading


def thread_with_named_parameters(**kwargs):
    print(threading.currentThread().getName(), 'Starting')
    print(kwargs['arg_1'])
    print(kwargs['arg_2'])


display_thread = threading.Thread(name="Kivy game display",
                                  target=thread_with_named_parameters,
                                  kwargs={'arg_1':'aaa', 'arg_2':'bbb'}).start()