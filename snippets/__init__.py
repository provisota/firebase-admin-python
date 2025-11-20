# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

# Placeholder for actual implementations of initialize_app, get_app, and delete_app

def initialize_app():
    pass

def get_app():
    pass

def delete_app():
    pass

from .analytics import Analytics

__all__ = ['initialize_app', 'get_app', 'delete_app', 'Analytics']
