# Copyright 2025 Sunil Sharma (https://github.com/sunbyte16/)
# All Rights Reserved.
#
#                     GNU GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007
#  Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
#  Everyone is permitted to copy and distribute verbatim copies
#  of this license document, but changing it is not allowed.
# ==============================================================================

from flask import Flask

app = Flask(__name__)

import src.views
