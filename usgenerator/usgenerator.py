#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from subjects import subjects
from verbs import verbs
from objects import objects
from environments import environments

import random


class MainPage(webapp.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Como ' + self.get_subject()
                                + ' quiero ' + self.get_verb()
                                + ' ' + self.get_objects()
                                + ' ' + self.get_environment())

    def get_subject(self):
        return subjects[self.get_random(len(subjects)-1)]

    def get_verb(self):
        return verbs[self.get_random(len(verbs)-1)]

    def get_objects(self):
        return objects[self.get_random(len(objects)-1)]

    def get_environment(self):
        return environments[self.get_random(len(environments)-1)]

    def get_random(self, size):
        return random.randint(0, size)

application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
