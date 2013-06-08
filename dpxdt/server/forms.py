#!/usr/bin/env python
# Copyright 2013 Brett Slatkin
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
# See the License for the specific language governing permissions and
# limitations under the License.

"""Forms for parsing and validating frontend requests."""

import datetime

# Local libraries
from flask.ext.wtf import (
    BooleanField, DataRequired, Form, HiddenField, IntegerField,
    Length, NumberRange, TextField)

# Local modules
from . import app


class BuildForm(Form):
    """Form for creating or editing a build."""

    name = TextField(validators=[Length(min=1, max=100)])


class ReleaseForm(Form):
    """Form for viewing or approving a release."""

    id = HiddenField(validators=[NumberRange(min=1)])
    name = HiddenField(validators=[Length(min=1)])
    number = HiddenField(validators=[NumberRange(min=1)])

    good = HiddenField()
    bad = HiddenField()
    reviewing = HiddenField()


class RunForm(Form):
    """Form for viewing or approving a run."""

    id = HiddenField(validators=[NumberRange(min=1)])
    name = HiddenField(validators=[Length(min=1)])
    number = HiddenField(validators=[NumberRange(min=1)])
    test = HiddenField(validators=[Length(min=1)])
    approve = HiddenField()
    disapprove = HiddenField()