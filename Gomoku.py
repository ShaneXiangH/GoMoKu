import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)


# don't change the class name
class AI(object):

    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
        # the max time you should use, your algorithm's run time must not exceed the time
        # limit
        self.time_out = time_out
        # You need to add your decision into your candidate_list.
        # System will get the end of your candidate_list as your decision.
        self.candidate_list = []

    def checkLine(self, i, j, chessboard):
        if i != self.chessboard_size - 1:
            # ^*
            if chessboard[i + 1][j] == self.color:
                if i != self.chessboard_size - 2:
                    # ^**
                    if chessboard[i + 2][j] == self.color:
                        if i != self.chessboard_size - 3:
                            # ^***
                            if chessboard[i + 3][j] == self.color:
                                if i != self.chessboard_size - 4:
                                    # ^****
                                    if chessboard[i + 4][j] == self.color:
                                        point_self = 1000000
                                    # ^***@
                                    elif chessboard[i + 4][j] == -self.color:
                                        if i != 0:
                                            # *^***@
                                            if chessboard[i - 1][j] == self.color:
                                                point_self = 1000000
                                            # @^***@
                                            elif chessboard[i - 1][j] == -self.color:
                                                point_self = 0
                                            # _^***@
                                            else:
                                                if i != 1:
                                                    # *_^***@
                                                    if chessboard[i - 2][j] == self.color:
                                                        point_self = 10000
                                                    # @_^***@ or __^***@ or |_^***@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                        # |^***@
                                        else:
                                            point_self = 0
                                    # ^***_
                                    else:
                                        if i != 0:
                                            # *^***_
                                            if chessboard[i - 1][j] == self.color:
                                                if i != 1:
                                                    # **^***_
                                                    if chessboard[i - 2][j] == self.color:
                                                        point_self = 1000000
                                                    # @*^***_ or _*^***_ or |*^***_
                                                    else:
                                                        point_self = 1000000
                                                else:
                                                    point_self = 1000000
                                            # @^***_
                                            elif chessboard[i - 1][j] == -self.color:
                                                point_self = 10000
                                            # _^***_
                                            else:
                                                point_self = 100000
                                        # |^***_
                                        else:
                                            point_self = 10000
                                # ^***|
                                else:
                                    if i != 0:
                                        # *^***|
                                        if chessboard[i - 1][j] == self.color:
                                            point_self = 1000000
                                        # @^***|
                                        elif chessboard[i - 1][j] == -self.color:
                                            point_self = 0
                                        # _^***|
                                        else:
                                            point_self = 10000
                                    # |^***|
                                    else:
                                        point_self = 0
                            # ^**@
                            elif chessboard[i + 3][j] == -self.color:
                                if i != 0:
                                    # *^**@
                                    if chessboard[i - 1][j] == self.color:
                                        if i != 1:
                                            # **^**@
                                            if chessboard[i - 2][j] == self.color:
                                                point_self = 1000000
                                            # @*^**@
                                            elif chessboard[i - 2][j] == -self.color:
                                                point_self = 0
                                            # _*^**@
                                            else:
                                                point_self = 10000
                                        # |^**@
                                        else:
                                            point_self = 0
                                    # @^**@
                                    elif chessboard[i - 1][j] == -self.color:
                                        point_self = 0
                                    # _^**@
                                    else:
                                        if i != 1:
                                            # *_^**@
                                            if chessboard[i - 2][j] == self.color:
                                                if i != 2:
                                                    # **_^**@
                                                    if chessboard[i - 3][j] == self.color:
                                                        point_self = 10000
                                                    # @*_^**@ or _*_^**@ or |*_^**@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @_^**@
                                            elif chessboard[i - 2][j] == -self.color:
                                                point_self = 0
                                            # __^**@
                                            else:
                                                if i != 2:
                                                    # *__^**@
                                                    if chessboard[i - 3][j] == self.color:
                                                        point_self = 1000
                                                    # @__^**@ or ___^**@ or |__^**@
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                        # |_^**@
                                        else:
                                            point_self = 0
                                # |^**@
                                else:
                                    point_self = 0
                            # ^**_
                            else:
                                if i != 0:
                                    # *^**_
                                    if chessboard[i - 1][j] == self.color:
                                        if i != 1:
                                            # **^**_
                                            if chessboard[i - 2][j] == self.color:
                                                if i != 2:
                                                    # ***^**_
                                                    if chessboard[i - 3][j] == self.color:
                                                        point_self = 1000000
                                                    # @**^**_ or _**^**_ or |**^**_
                                                    else:
                                                        point_self = 1000000
                                                else:
                                                    point_self = 1000000
                                            # @*^**_
                                            elif chessboard[i - 2][j] == -self.color:
                                                if i != self.chessboard_size - 4:
                                                    # @*^**_*
                                                    if chessboard[i + 4][j] == self.color:
                                                        point_self = 10000
                                                    # @*^**_@ or @*^**__ or @*^**_|
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # _*^**_
                                            else:
                                                point_self = 100000
                                        # |*^**_
                                        else:
                                            point_self = 10000
                                    # @^**_
                                    elif chessboard[i - 1][j] == -self.color:
                                        point_self = 1000
                                    # _^**_
                                    else:
                                        if i != 1:
                                            # *_^**_
                                            if chessboard[i - 2][j] == self.color:
                                                point_self = 10000
                                            # @_^**_
                                            elif chessboard[i - 2][j] == -self.color:
                                                point_self = 10000
                                            # __^**_
                                            else:
                                                if i != 2:
                                                    # *__^**_
                                                    if chessboard[i - 3][j] == self.color:
                                                        point_self = 10000
                                                    # @__^**_
                                                    elif chessboard[i - 3][j] == -self.color:
                                                        point_self = 10000
                                                    # ___^**_
                                                    else:
                                                        point_self = 10000
                                                # |__^**_
                                                else:
                                                    point_self = 10000
                                        # |_^**_
                                        else:
                                            point_self = 1000
                                # |^**_
                                else:
                                    point_self = 1000
                        # ^**|
                        else:
                            if i != 0:
                                # *^**|
                                if chessboard[i - 1][j] == self.color:
                                    if i != 1:
                                        # **^**|
                                        if chessboard[i - 2][j] == self.color:
                                            point_self = 1000000
                                        # @*^**|
                                        elif chessboard[i - 2][j] == -self.color:
                                            point_self = 0
                                        # _*^**|
                                        else:
                                            point_self = 10000
                                    # |*^**|
                                    else:
                                        point_self = 0
                                # @^**|
                                elif chessboard[i - 1][j] == -self.color:
                                    point_self = 0
                                # _^**|
                                else:
                                    if i != 1:
                                        # *_^**|
                                        if chessboard[i - 2][j] == self.color:
                                            point_self = 10000
                                        # @_^**|
                                        elif chessboard[i - 2][j] == -self.color:
                                            point_self = 0
                                        # __^**|
                                        else:
                                            point_self = 1000
                                    # |_^**|
                                    else:
                                        point_self = 0
                            # |^**|
                            else:
                                point_self = 0
                    # ^*@
                    elif chessboard[i + 2][j] == -self.color:
                        if i != 0:
                            # *^*@
                            if chessboard[i - 1][j] == self.color:
                                if i != 1:
                                    # **^*@
                                    if chessboard[i - 2][j] == self.color:
                                        if i != 2:
                                            # ***^*@
                                            if chessboard[i - 3][j] == self.color:
                                                point_self = 1000000
                                            # @**^*@
                                            elif chessboard[i - 3][j] == -self.color:
                                                point_self = 0
                                            # _**^*@
                                            else:
                                                point_self = 10000
                                        # |**^*@
                                        else:
                                            point_self = 0
                                    # @*^*@
                                    elif chessboard[i - 2][j] == -self.color:
                                        point_self = 0
                                    # _*^*@
                                    else:
                                        if i != 2:
                                            # *_*^*@
                                            if chessboard[i - 3][j] == self.color:
                                                if i != 3:
                                                    # **_*^*@
                                                    if chessboard[i - 4][j] == self.color:
                                                        point_self = 10000
                                                    # @*_*^*@ or _*_*^*@ or |*_*^*@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @_*^*@
                                            elif chessboard[i - 3][j] == -self.color:
                                                point_self = 0
                                            # __*^*@
                                            else:
                                                if i != 3:
                                                    # *__*^*@
                                                    if chessboard[i - 4][j] == self.color:
                                                        point_self = 1000
                                                    # @__*^*@ or ___*^*@ or |__*^*@
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                        # |_*^*@
                                        else:
                                            point_self = 0
                                # |*^*@
                                else:
                                    point_self = 0
                            # @^*@
                            elif chessboard[i - 1][j] == -self.color:
                                point_self = 0
                            # _^*@
                            else:
                                if i != 1:
                                    # *_^*@
                                    if chessboard[i - 2][j] == self.color:
                                        if i != 2:
                                            # **_^*@
                                            if chessboard[i - 3][j] == self.color:
                                                if i != 3:
                                                    # ***_^*@
                                                    if chessboard[i - 4][j] == self.color:
                                                        point_self = 10000
                                                    # @**_^*@ or _**_^*@ or |**_^*@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @*_^*@
                                            elif chessboard[i - 3][j] == -self.color:
                                                point_self = 0
                                            # _*_^*@
                                            else:
                                                if i != 3:
                                                    # *_*_^*@
                                                    if chessboard[i - 4][j] == self.color:
                                                        point_self = 1000
                                                    # @_*_^*@ or __*_^*@ or |_*_^*@
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                        # |*_^*@
                                        else:
                                            point_self = 0
                                    # @_^*@
                                    elif chessboard[i - 2][j] == -self.color:
                                        point_self = 0
                                    # __^*@
                                    else:
                                        if i != 2:
                                            # *__^*@
                                            if chessboard[i - 3][j] == self.color:
                                                if i != 3:
                                                    # **__^*@
                                                    if chessboard[i - 4][j] == self.color:
                                                        point_self = 1000
                                                    # @*__^*@ or _*__^* or |*__^*
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                            # @__^*@
                                            elif chessboard[i - 3][j] == -self.color:
                                                point_self = 0
                                            # ___^*@
                                            else:
                                                if i != 3:
                                                    # *___^*@
                                                    if chessboard[i - 4][j] == self.color:
                                                        point_self = 0
                                                    # @___^*@ or ____^*@ or |___^*@
                                                    else:
                                                        point_self = 100
                                                else:
                                                    point_self = 10
                                        # |__^*@
                                        else:
                                            point_self = 0
                                # |_^*@
                                else:
                                    point_self = 0
                        # |^*@
                        else:
                            point_self = 0
                    # ^*_
                    else:
                        if i != self.chessboard_size - 3:
                            # ^*_*
                            if chessboard[i + 3][j] == self.color:
                                if i != 0:
                                    # *^*_*
                                    if chessboard[i - 1][j] == self.color:
                                        if i != 1:
                                            # **^*_*
                                            if chessboard[i - 2][j] == self.color:
                                                if i != 2:
                                                    # ***^*_*
                                                    if chessboard[i - 3][j] == self.color:
                                                        if i != 3:
                                                            # ****^*_*
                                                            if chessboard[i - 4][j] == self.color:
                                                                point_self = 1000000
                                                            # @***^*_* or _***^*_* or |***^*_*
                                                            else:
                                                                point_self = 1000000
                                                        else:
                                                            point_self = 1000000
                                                    # @**^*_*
                                                    elif chessboard[i - 3][j] == -self.color:
                                                        point_self = 10000
                                                    # _**^*_*
                                                    else:
                                                        if i != 3:
                                                            # *_**^*_*
                                                            if chessboard[i - 4][j] == self.color:
                                                                point_self = 1000000
                                                            # @_**^*_* or __**^*_* or |_**^*_*
                                                            else:
                                                                point_self = 1000000
                                                        else:
                                                            point_self = 1000000
                                                # |**^*_*
                                                else:
                                                    point_self = 10000
                                            # @*^*_*
                                            elif chessboard[i - 2][j] == -self.color:
                                                if i != self.chessboard_size - 4:
                                                    # @*^*_**
                                                    if chessboard[i + 4][j] == self.color:
                                                        point_self = 10000
                                                    # @*^*_*@ or @*^*_*_ or @*^*_*|
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # _*^*_*
                                            else:
                                                if i != 2:
                                                    # *_*^*_*
                                                    if chessboard[i - 3][j] == self.color:
                                                        # **_*^*_**
                                                        if i != self.chessboard_size - 4 \
                                                                and i != 3 \
                                                                and chessboard[i - 4][j] == self.color \
                                                                and chessboard[i + 4][j] == self.color:
                                                            point_self = 100000
                                                        else:
                                                            point_self = 100000
                                                    # @_*^*_* or __*^*_*
                                                    else:
                                                        if i != self.chessboard_size - 4:
                                                            # @_*^*_** or __*^*_**
                                                            if chessboard[i + 4][j] == self.color:
                                                                point_self = 10000
                                                            # @_*^*_*@ or @_*^*_*_ or @_*^*_*| or
                                                            # __*^*_*@ or __*^*_*_ or __*^*_*|
                                                            else:
                                                                point_self = 10000
                                                        else:
                                                            point_self = 10000
                                                # |_*^*_*
                                                else:
                                                    if i != self.chessboard_size - 4:
                                                        # |_*^*_**
                                                        if chessboard[i + 4][j] == self.color:
                                                            point_self = 10000
                                                        # |_*^*_*@ or |_*^*_*_ or |_*^*_*|
                                                        else:
                                                            point_self = 10000
                                                    else:
                                                        point_self = 10000
                                        # |*^*_*
                                        else:
                                            if i != self.chessboard_size - 4:
                                                # |*^*_**
                                                if chessboard[i + 4][j] == self.color:
                                                    point_self = 0
                                                # |*^*_*@ or |*^*_*_ or |*^*_*|
                                                else:
                                                    point_self = 10000
                                            else:
                                                point_self = 10000
                                    # @^*_*
                                    elif chessboard[i - 1][j] == -self.color:
                                        if i != self.chessboard_size - 4:
                                            # @^*_**
                                            if chessboard[i + 4][j] == self.color:
                                                # @^*_***
                                                if i != self.chessboard_size - 5 and \
                                                        chessboard[i + 5][j] == self.color:
                                                    point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @^*_*@
                                            elif chessboard[i + 4][j] == -self.color:
                                                point_self = 0
                                            # @^*_*_
                                            else:
                                                point_self = 100
                                        # @^*_*|
                                        else:
                                            point_self = 0
                                    # _^*_*
                                    else:
                                        if i != 1:
                                            # *_^*_*
                                            if chessboard[i - 2][j] == self.color:
                                                point_self = 10000
                                            # @_^*_*
                                            elif chessboard[i - 2][j] == -self.color:
                                                point_self = 10000
                                            # __^*_*
                                            else:
                                                point_self = 10000
                                        # |_^*_*
                                        else:
                                            point_self = 10000
                                # |^*_*
                                else:
                                    point_self = 10
                            # ^*_@
                            elif chessboard[i + 3][j] == -self.color:
                                if i != 0:
                                    # *^*_@
                                    if chessboard[i - 1][j] == self.color:
                                        if i != 1:
                                            # **^*_@
                                            if chessboard[i - 2][j] == self.color:
                                                if i != 2:
                                                    # ***^*_@
                                                    if chessboard[i - 3][j] == self.color:
                                                        # ****^*_@
                                                        if i != 3 and \
                                                                chessboard[i - 4][j] == self.color:
                                                            point_self = 1000000
                                                        else:
                                                            point_self = 1000000
                                                    # @**^*_@
                                                    elif chessboard[i - 3][j] == -self.color:
                                                        point_self = 10000
                                                    # _**^*_@
                                                    else:
                                                        point_self = 100000
                                                # |**^*_@
                                                else:
                                                    point_self = 10000
                                            # @*^*_@
                                            elif chessboard[i - 2][j] == -self.color:
                                                point_self = 0
                                            # _*^*_@
                                            else:
                                                point_self = 10000
                                        # |*^*_@
                                        else:
                                            point_self = 0
                                    # @^*_@
                                    elif chessboard[i - 1][j] == -self.color:
                                        point_self = 0
                                    # _^*_@
                                    else:
                                        point_self = 1000
                                # |^*_@
                                else:
                                    point_self = 0
                            # ^*__
                            else:
                                if i != 0:
                                    # *^*__
                                    if chessboard[i - 1][j] == self.color:
                                        if i != 1:
                                            # **^*__
                                            if chessboard[i - 2][j] == self.color:
                                                if i != 2:
                                                    # ***^*__
                                                    if chessboard[i - 3][j] == self.color:
                                                        if i != 3:
                                                            # ****^*__
                                                            if chessboard[i - 4][j] == self.color:
                                                                point_self = 1000000
                                                            # @***^*_ or _***^*_ or |***^*_
                                                            else:
                                                                point_self = 1000000
                                                        else:
                                                            point_self = 1000000
                                                    # @**^*__
                                                    elif chessboard[i - 3][j] == -self.color:
                                                        point_self = 10000
                                                    # _**^*__
                                                    else:
                                                        point_self = 100000
                                                # |**^*__
                                                else:
                                                    point_self = 10000
                                            # @*^*__
                                            elif chessboard[i - 3][j] == -self.color:
                                                if i != self.chessboard_size - 4:
                                                    # @*^*__*
                                                    if chessboard[i + 4][j] == self.color:
                                                        point_self = 0
                                                    # @*^*__@ or @*^*___ or @*^*__|
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                            # _*^*__
                                            else:
                                                if i != 2:
                                                    # *_*^*__
                                                    if chessboard[i - 3][j] == self.color:
                                                        if i != 3:
                                                            # **_*^*__
                                                            if chessboard[i - 4][j] == self.color:
                                                                if i != self.chessboard_size - 4:
                                                                    # **_*^*__*
                                                                    if chessboard[i + 4][j] == self.color:
                                                                        point_self = 10000
                                                                    # **_*^*__@ or **_*^*___ or **_*^*__|
                                                                    else:
                                                                        point_self = 10000
                                                                else:
                                                                    point_self = 10000
                                                            # @*_*^*__ or _*_*^*__ or |*_*^*__
                                                            else:
                                                                point_self = 10000
                                                        else:
                                                            point_self = 10000
                                                    # @_*^*__ or  __*^*__  or |_*^*__
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000

                                        # |*^*__
                                        else:
                                            if i != self.chessboard_size - 4:
                                                # |*^*__*
                                                if chessboard[i + 4][j] == self.color:
                                                    point_self = 1000
                                                # |*^*__@ or |*^*___ or |*^*__|
                                                else:
                                                    point_self = 1000
                                            else:
                                                point_self = 1000
                                    # @^*__
                                    elif chessboard[i - 1][j] == -self.color:
                                        point_self = 0
                                    # _^*__
                                    else:
                                        point_self = 1000
                                # |^*__
                                else:
                                    point_self = 1
                        # ^*_|
                        else:
                            if i != 0:
                                # *^*_|
                                if chessboard[i - 1][j] == self.color:
                                    if i != 1:
                                        # **^*_|
                                        if chessboard[i - 2][j] == self.color:
                                            point_self = 100000
                                        # @*^*_|
                                        elif chessboard[i - 2][j] == -self.color:
                                            point_self = 0
                                        # _*^*_|
                                        else:
                                            if i != 2:
                                                # *_*^*_|
                                                if chessboard[i - 3][j] == self.color:
                                                    # **_*^*|
                                                    if i != 3 and \
                                                            chessboard[i - 4][j] == self.color:
                                                        point_self = 10000
                                                    else:
                                                        point_self = 10000
                                                # @_*^*_| or __*^*_| or |_*^*_|
                                                else:
                                                    point_self = 10000
                                            else:
                                                point_self = 10000
                                    # |*^*_|
                                    else:
                                        point_self = 0
                                # @^*_|
                                elif chessboard[i - 1][j] == -self.color:
                                    point_self = 0
                                # _^*_|
                                else:
                                    point_self = 1000
                            # |^*_|
                            else:
                                point_self = 0
                # ^*|
                else:
                    if i != 0:
                        # *^*|
                        if chessboard[i - 1][j] == self.color:
                            if i != 1:
                                # **^*|
                                if chessboard[i - 2][j] == self.color:
                                    if i != 2:
                                        # ***^*|
                                        if chessboard[i - 3][j] == self.color:
                                            # ****^*|
                                            if i != 3 and \
                                                    chessboard[i - 4][j] == self.color:
                                                point_self = 1000000
                                            else:
                                                point_self = 1000000
                                        # @**^*|
                                        elif chessboard[i - 3][j] == -self.color:
                                            point_self = 0
                                        # _**^*|
                                        else:
                                            # *_**^*|
                                            if i != 3 and \
                                                    chessboard[i - 4][j] == self.color:
                                                point_self = 10000
                                            else:
                                                point_self = 10000
                                    # |**^*|
                                    else:
                                        point_self = 0
                                # @*^*|
                                elif chessboard[i - 2][j] == -self.color:
                                    point_self = 0
                                # _*^*|
                                else:
                                    if i != 2:
                                        # *_*^*|
                                        if chessboard[i - 3][j] == self.color:
                                            point_self = 10000
                                        # @_*^*|
                                        elif chessboard[i - 3][j] == -self.color:
                                            point_self = 0
                                        # __*^*|
                                        else:
                                            # *__*^*|
                                            if i != 3 and \
                                                    chessboard[i - 4][j] == self.color:
                                                point_self = 1000
                                            else:
                                                point_self = 1000
                                    # |_*^*|
                                    else:
                                        point_self = 0
                            # |*^*|
                            else:
                                point_self = 0
                        # @^*|
                        elif chessboard[i - 1][j] == -self.color:
                            point_self = 0
                        # _^*|
                        else:
                            if i != 1:
                                # *_^*|
                                if chessboard[i - 2][j] == self.color:
                                    if i != 2:
                                        # **_^*|
                                        if chessboard[i - 3][j] == self.color:
                                            # ***_^*|
                                            if i != 3 and \
                                                    chessboard[i - 4][j] == self.color:
                                                point_self = 10000
                                            else:
                                                point_self = 10000
                                        # @*_^*|
                                        elif chessboard[i - 3][j] == -self.color:
                                            point_self = 0
                                        # _*_^*|
                                        else:
                                            # *_*_^*|
                                            if i != 3 and \
                                                    chessboard[i - 4][j] == self.color:
                                                point_self = 1000
                                            else:
                                                point_self = 1000
                                    # |*_^*|
                                    else:
                                        point_self = 0
                                # @_^*|
                                elif chessboard[i - 2][j] == -self.color:
                                    point_self = 0
                                # __^*|
                                else:
                                    if i != 2:
                                        #  *__^*|
                                        if chessboard[i - 3][j] == self.color:
                                            # **__^*|
                                            if i != 3 and \
                                                    chessboard[i - 4][j] == self.color:
                                                point_self = 1000
                                            else:
                                                point_self = 1000
                                        # @__^*|
                                        elif chessboard[i - 3][j] == -self.color:
                                            point_self = 0
                                        # ___^*|
                                        else:
                                            # *___^*|
                                            if i != 3 and \
                                                    chessboard[i - 4][j] == self.color:
                                                point_self = 100
                                            else:
                                                point_self = 100
                                    # |__^*|
                                    else:
                                        point_self = 0
                            # |_^*|
                            else:
                                point_self = 0
                    # |^*|
                    else:
                        point_self = 0
            # ^@
            elif chessboard[i + 1][j] == -self.color:
                if i != 0:
                    # *^@
                    if chessboard[i - 1][j] == self.color:
                        if i != 1:
                            # **^@
                            if chessboard[i - 2][j] == self.color:
                                if i != 2:
                                    # ***^@
                                    if chessboard[i - 3][j] == self.color:
                                        if i != 3:
                                            # ****^@
                                            if chessboard[i - 4][j] == self.color:
                                                point_self = 1000000
                                            # @***^@
                                            elif chessboard[i - 4][j] == -self.color:
                                                point_self = 0
                                            # _***^@
                                            else:
                                                # *_***^@
                                                if i != 4 and \
                                                        chessboard[i - 5][j] == self.color:
                                                    point_self = 10000
                                                else:
                                                    point_self = 10000
                                        # |***^@
                                        else:
                                            point_self = 0
                                    # @**^@
                                    elif chessboard[i - 3][j] == -self.color:
                                        point_self = 0
                                    # _**^@
                                    else:
                                        point_self = 1000
                                # |**^@
                                else:
                                    point_self = 0
                            # @*^@
                            elif chessboard[i - 2][j] == -self.color:
                                point_self = 0
                            # _*^@
                            else:
                                if i != 2:
                                    # *_*^@
                                    if chessboard[i - 3][j] == self.color:
                                        point_self = 1000
                                    # @_*^@
                                    elif chessboard[i - 3][j] == -self.color:
                                        point_self = 0
                                    # __*^@
                                    else:
                                        point_self = 100
                                # |_*^@
                                else:
                                    point_self = 0
                        # |*^@
                        else:
                            point_self = 0
                    # @^@
                    elif chessboard[i - 1][j] == -self.color:
                        point_self = 0
                    # _^@
                    else:
                        if i != 1:
                            # *_^@
                            if chessboard[i - 2][j] == self.color:
                                point_self = 0
                            # @_^@
                            elif chessboard[i - 2][j] == -self.color:
                                point_self = 0
                            # __^@
                            else:
                                point_self = 1
                        # |_^@
                        else:
                            point_self = 0
                # |^@
                else:
                    point_self = 0
            # ^_
            else:
                if i != self.chessboard_size - 2:
                    # ^_*
                    if chessboard[i + 2][j] == self.color:
                        if i != 0:
                            # *^_*
                            if chessboard[i - 1][j] == self.color:
                                if i != 1:
                                    # **^_*
                                    if chessboard[i - 2][j] == self.color:
                                        if i != 2:
                                            # ***^_*
                                            if chessboard[i - 3][j] == self.color:
                                                if i != 3:
                                                    # ****^_*
                                                    if chessboard[i - 4][j] == self.color:
                                                        point_self = 1000000
                                                    # @***^_*
                                                    elif chessboard[i - 4][j] == self.color:
                                                        point_self = 10000
                                                    # _***^_*
                                                    else:
                                                        # *_***^_*
                                                        if i != 4 and \
                                                                chessboard[i - 5][j] == self.color:
                                                            point_self = 100000
                                                        else:
                                                            point_self = 100000
                                                # |***^_*
                                                else:
                                                    point_self = 10000
                                            # @**^_*
                                            elif chessboard[i - 3][j] == -self.color:
                                                # @**^_**
                                                if i != self.chessboard_size - 3 and \
                                                        chessboard[i + 3][j] == self.color:
                                                    point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # _**^_*
                                            else:
                                                point_self = 10000
                                        # |**^_*
                                        else:
                                            point_self = 10000
                                    # @*^_*
                                    elif chessboard[i - 2][j] == -self.color:
                                        point_self = 10
                                    # _*^_*
                                    else:
                                        point_self = 10000
                                # |*^_*
                                else:
                                    point_self = 100
                            # @^_*
                            elif chessboard[i - 1][j] == -self.color:
                                point_self = 0
                            # _^_*
                            else:
                                point_self = 0
                        # |^_*
                        else:
                            point_self = 0
                    # ^_@
                    elif chessboard[i + 2][j] == -self.color:
                        if i != 0:
                            # *^_@
                            if chessboard[i - 1][j] == self.color:
                                if i != 1:
                                    # **^_@
                                    if chessboard[i - 2][j] == self.color:
                                        if i != 2:
                                            # ***^_@
                                            if chessboard[i - 3][j] == self.color:
                                                if i != 3:
                                                    # ****^_@
                                                    if chessboard[i - 4][j] == self.color:
                                                        point_self = 1000000
                                                    # @***^_@
                                                    elif chessboard[i - 4][j] == -self.color:
                                                        point_self = 10000
                                                    # _***^_@
                                                    else:
                                                        point_self = 100000
                                                # |***^_@
                                                else:
                                                    point_self = 10000
                                            # @**^_@
                                            elif chessboard[i - 3][j] == -self.color:
                                                point_self = 0
                                            # _**^_@
                                            else:
                                                point_self = 10000
                                        # |**^_@
                                        else:
                                            point_self = 0
                                    # @*^_@
                                    elif chessboard[i - 2][j] == -self.color:
                                        point_self = 0
                                    # _*^_@
                                    else:
                                        point_self = 100
                                # |*^_@
                                else:
                                    point_self = 0
                            # @^_@
                            elif chessboard[i - 1][j] == -self.color:
                                point_self = 0
                            # _^_@
                            else:
                                point_self = 1
                        # |^_@
                        else:
                            point_self = 0
                    # ^__
                    else:
                        if i != 0:
                            # *^__
                            if chessboard[i - 1][j] == self.color:
                                if i != 1:
                                    # **^__
                                    if chessboard[i - 2][j] == self.color:
                                        if i != 2:
                                            # ***^__
                                            if chessboard[i - 3][j] == self.color:
                                                if i != 3:
                                                    # ****^__
                                                    if chessboard[i - 4][j] == self.color:
                                                        point_self = 1000000
                                                    # @***^__
                                                    elif chessboard[i - 4][j] == -self.color:
                                                        point_self = 10000
                                                    # _***^__
                                                    else:
                                                        point_self = 100000
                                                # |***^__
                                                else:
                                                    point_self = 10000
                                            # @**^__
                                            elif chessboard[i - 3][j] == -self.color:
                                                point_self = 1000
                                            # _**^__
                                            else:
                                                point_self = 10000
                                        # |**^__
                                        else:
                                            point_self = 1000
                                    # @*^__
                                    elif chessboard[i - 2][j] == -self.color:
                                        point_self = 10
                                    # _*^__
                                    else:
                                        if i != 2:
                                            # *_*^__
                                            if chessboard[i - 3][j] == self.color:
                                                point_self = 1000
                                            # @_*^__
                                            elif chessboard[i - 3][j] == -self.color:
                                                point_self = 1000
                                            # __*^__
                                            else:
                                                point_self = 1000
                                        # |_*^__
                                        else:
                                            point_self = 1000
                                # |*^__
                                else:
                                    point_self = 100
                            # @^__
                            elif chessboard[i - 1][j] == -self.color:
                                point_self = 1
                            # _^__
                            else:
                                point_self = 2
                        # |^__
                        else:
                            point_self = 0
                # ^_|
                else:
                    if i != 0:
                        # *^_|
                        if chessboard[i - 1][j] == self.color:
                            if i != 1:
                                # **^_|
                                if chessboard[i - 2][j] == self.color:
                                    if i != 2:
                                        # ***^_|
                                        if chessboard[i - 3][j] == self.color:
                                            if i != 3:
                                                # ****^_|
                                                if chessboard[i - 4][j] == self.color:
                                                    point_self = 1000000
                                                # @***^_|
                                                elif chessboard[i - 4][j] == -self.color:
                                                    point_self = 10000
                                                # _***^_|
                                                else:
                                                    point_self = 100000
                                            # |***^_|
                                            else:
                                                point_self = 10000
                                        # @**^_|
                                        elif chessboard[i - 3][j] == -self.color:
                                            point_self = 0
                                        # _**^_|
                                        else:
                                            point_self = 10000
                                    # |**^_|
                                    else:
                                        point_self = 0
                                # @*^_|
                                elif chessboard[i - 2][j] == -self.color:
                                    point_self = 0
                                # _*^_|
                                else:
                                    # *_*^_|
                                    if i != 2 and \
                                            chessboard[i - 3][j] == self.color:
                                        point_self = 1000
                                    else:
                                        point_self = 1000
                            # |*^_|
                            else:
                                point_self = 0
                        # @^_|
                        elif chessboard[i - 1][j] == -self.color:
                            point_self = 0
                        # _^_|
                        else:
                            point_self = 0
                    # |^_|
                    else:
                        point_self = 0
        # ^|
        else:
            if i != 0:
                # *^|
                if chessboard[i - 1][j] == self.color:
                    if i != 1:
                        # **^|
                        if chessboard[i - 2][j] == self.color:
                            if i != 2:
                                # ***^|
                                if chessboard[i - 3][j] == self.color:
                                    if i != 3:
                                        # ****^|
                                        if chessboard[i - 4][j] == self.color:
                                            point_self = 1000000
                                        # @***^|
                                        elif chessboard[i - 4][j] == -self.color:
                                            point_self = 0
                                        # _***^|
                                        else:
                                            # *_***^|
                                            if i != 4 and \
                                                    chessboard[i - 5][j] == self.color:
                                                point_self = 10000
                                            else:
                                                point_self = 10000
                                    # |***^|
                                    else:
                                        point_self = 0
                                # @**^|
                                elif chessboard[i - 3][j] == -self.color:
                                    point_self = 0
                                # _**^|
                                else:
                                    point_self = 0
                            # |**^|
                            else:
                                point_self = 0
                        # @*^|
                        elif chessboard[i - 2][j] == -self.color:
                            point_self = 0
                        # _*^|
                        else:
                            point_self = 0
                    # |*^|
                    else:
                        point_self = 0
                # @^|
                elif chessboard[i - 1][j] == -self.color:
                    point_self = 0
                # _^|
                else:
                    point_self = 0
            # |^|
            else:
                point_self = 0
        return point_self

    def checkRow(self, i, j, chessboard):
        if j != self.chessboard_size - 1:
            # ^*
            if chessboard[i][j + 1] == self.color:
                if j != self.chessboard_size - 2:
                    # ^**
                    if chessboard[i][j + 2] == self.color:
                        if j != self.chessboard_size - 3:
                            # ^***
                            if chessboard[i][j + 3] == self.color:
                                if j != self.chessboard_size - 4:
                                    # ^****
                                    if chessboard[i][j + 4] == self.color:
                                        point_self = 1000000
                                    # ^***@
                                    elif chessboard[i][j + 4] == -self.color:
                                        if j != 0:
                                            # *^***@
                                            if chessboard[i][j - 1] == self.color:
                                                point_self = 1000000
                                            # @^***@
                                            elif chessboard[i][j - 1] == -self.color:
                                                point_self = 0
                                            # _^***@
                                            else:
                                                if j != 1:
                                                    # *_^***@
                                                    if chessboard[i][j - 2] == self.color:
                                                        point_self = 10000
                                                    # @_^***@ or __^***@ or |_^***@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                        # |^***@
                                        else:
                                            point_self = 0
                                    # ^***_
                                    else:
                                        if j != 0:
                                            # *^***_
                                            if chessboard[i][j - 1] == self.color:
                                                if j != 1:
                                                    # **^***_
                                                    if chessboard[i][j - 2] == self.color:
                                                        point_self = 1000000
                                                    # @*^***_ or _*^***_ or |*^***_
                                                    else:
                                                        point_self = 1000000
                                                else:
                                                    point_self = 1000000
                                            # @^***_
                                            elif chessboard[i][j - 1] == -self.color:
                                                point_self = 10000
                                            # _^***_
                                            else:
                                                point_self = 100000
                                        # |^***_
                                        else:
                                            point_self = 10000
                                # ^***|
                                else:
                                    if j != 0:
                                        # *^***|
                                        if chessboard[i][j - 1] == self.color:
                                            point_self = 1000000
                                        # @^***|
                                        elif chessboard[i][j - 1] == -self.color:
                                            point_self = 0
                                        # _^***|
                                        else:
                                            point_self = 10000
                                    # |^***|
                                    else:
                                        point_self = 0
                            # ^**@
                            elif chessboard[i][j + 3] == -self.color:
                                if j != 0:
                                    # *^**@
                                    if chessboard[i][j - 1] == self.color:
                                        if j != 1:
                                            # **^**@
                                            if chessboard[i][j - 2] == self.color:
                                                point_self = 1000000
                                            # @*^**@
                                            elif chessboard[i][j - 2] == -self.color:
                                                point_self = 0
                                            # _*^**@
                                            else:
                                                point_self = 10000
                                        # |^**@
                                        else:
                                            point_self = 0
                                    # @^**@
                                    elif chessboard[i][j - 1] == -self.color:
                                        point_self = 0
                                    # _^**@
                                    else:
                                        if j != 1:
                                            # *_^**@
                                            if chessboard[i][j - 2] == self.color:
                                                if j != 2:
                                                    # **_^**@
                                                    if chessboard[i][j - 3] == self.color:
                                                        point_self = 10000
                                                    # @*_^**@ or _*_^**@ or |*_^**@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @_^**@
                                            elif chessboard[i][j - 2] == -self.color:
                                                point_self = 0
                                            # __^**@
                                            else:
                                                if j != 2:
                                                    # *__^**@
                                                    if chessboard[i][j - 3] == self.color:
                                                        point_self = 1000
                                                    # @__^**@ or ___^**@ or |__^**@
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                        # |_^**@
                                        else:
                                            point_self = 0
                                # |^**@
                                else:
                                    point_self = 0
                            # ^**_
                            else:
                                if j != 0:
                                    # *^**_
                                    if chessboard[i][j - 1] == self.color:
                                        if j != 1:
                                            # **^**_
                                            if chessboard[i][j - 2] == self.color:
                                                if j != 2:
                                                    # ***^**_
                                                    if chessboard[i][j - 3] == self.color:
                                                        point_self = 1000000
                                                    # @**^**_ or _**^**_ or |**^**_
                                                    else:
                                                        point_self = 1000000
                                                else:
                                                    point_self = 1000000
                                            # @*^**_
                                            elif chessboard[i][j - 2] == -self.color:
                                                if j != self.chessboard_size - 4:
                                                    # @*^**_*
                                                    if chessboard[i][j + 4] == self.color:
                                                        point_self = 10000
                                                    # @*^**_@ or @*^**__ or @*^**_|
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # _*^**_
                                            else:
                                                point_self = 100000
                                        # |*^**_
                                        else:
                                            point_self = 10000
                                    # @^**_
                                    elif chessboard[i][j - 1] == -self.color:
                                        point_self = 100
                                    # _^**_
                                    else:
                                        if j != 1:
                                            # *_^**_
                                            if chessboard[i][j - 2] == self.color:
                                                point_self = 10000
                                            # @_^**_
                                            elif chessboard[i][j - 2] == -self.color:
                                                point_self = 10000
                                            # __^**_
                                            else:
                                                if j != 2:
                                                    # *__^**_
                                                    if chessboard[i][j - 3] == self.color:
                                                        point_self = 10000
                                                    # @__^**_
                                                    elif chessboard[i][j - 3] == -self.color:
                                                        point_self = 10000
                                                    # ___^**_
                                                    else:
                                                        point_self = 10000
                                                # |__^**_
                                                else:
                                                    point_self = 10000
                                        # |_^**_
                                        else:
                                            point_self = 10000
                                # |^**_
                                else:
                                    point_self = 1000
                        # ^**|
                        else:
                            if j != 0:
                                # *^**|
                                if chessboard[i][j - 1] == self.color:
                                    if j != 1:
                                        # **^**|
                                        if chessboard[i][j - 2] == self.color:
                                            point_self = 1000000
                                        # @*^**|
                                        elif chessboard[i][j - 2] == -self.color:
                                            point_self = 0
                                        # _*^**|
                                        else:
                                            point_self = 10000
                                    # |*^**|
                                    else:
                                        point_self = 0
                                # @^**|
                                elif chessboard[i][j - 1] == -self.color:
                                    point_self = 0
                                # _^**|
                                else:
                                    if j != 1:
                                        # *_^**|
                                        if chessboard[i][j - 2] == self.color:
                                            point_self = 10000
                                        # @_^**|
                                        elif chessboard[i][j - 2] == -self.color:
                                            point_self = 0
                                        # __^**|
                                        else:
                                            point_self = 1000
                                    # |_^**|
                                    else:
                                        point_self = 0
                            # |^**|
                            else:
                                point_self = 0
                    # ^*@
                    elif chessboard[i][j + 2] == -self.color:
                        if j != 0:
                            # *^*@
                            if chessboard[i][j - 1] == self.color:
                                if j != 1:
                                    # **^*@
                                    if chessboard[i][j - 2] == self.color:
                                        if j != 2:
                                            # ***^*@
                                            if chessboard[i][j - 3] == self.color:
                                                point_self = 1000000
                                            # @**^*@
                                            elif chessboard[i][j - 3] == -self.color:
                                                point_self = 0
                                            # _**^*@
                                            else:
                                                point_self = 10000
                                        # |**^*@
                                        else:
                                            point_self = 0
                                    # @*^*@
                                    elif chessboard[i][j - 2] == -self.color:
                                        point_self = 0
                                    # _*^*@
                                    else:
                                        if j != 2:
                                            # *_*^*@
                                            if chessboard[i][j - 3] == self.color:
                                                if j != 3:
                                                    # **_*^*@
                                                    if chessboard[i][j - 4] == self.color:
                                                        point_self = 10000
                                                    # @*_*^*@ or _*_*^*@ or |*_*^*@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @_*^*@
                                            elif chessboard[i][j - 3] == -self.color:
                                                point_self = 0
                                            # __*^*@
                                            else:
                                                if j != 3:
                                                    # *__*^*@
                                                    if chessboard[i][j - 4] == self.color:
                                                        point_self = 1000
                                                    # @__*^*@ or ___*^*@ or |__*^*@
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                        # |_*^*@
                                        else:
                                            point_self = 0
                                # |*^*@
                                else:
                                    point_self = 0
                            # @^*@
                            elif chessboard[i][j - 1] == -self.color:
                                point_self = 0
                            # _^*@
                            else:
                                if j != 1:
                                    # *_^*@
                                    if chessboard[i][j - 2] == self.color:
                                        if j != 2:
                                            # **_^*@
                                            if chessboard[i][j - 3] == self.color:
                                                if j != 3:
                                                    # ***_^*@
                                                    if chessboard[i][j - 4] == self.color:
                                                        point_self = 10000
                                                    # @**_^*@ or _**_^*@ or |**_^*@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @*_^*@
                                            elif chessboard[i][j - 3] == -self.color:
                                                point_self = 0
                                            # _*_^*@
                                            else:
                                                if j != 3:
                                                    # *_*_^*@
                                                    if chessboard[i][j - 4] == self.color:
                                                        point_self = 100
                                                    # @_*_^*@ or __*_^*@ or |_*_^*@
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                        # |*_^*@
                                        else:
                                            point_self = 0
                                    # @_^*@
                                    elif chessboard[i][j - 2] == -self.color:
                                        point_self = 0
                                    # __^*@
                                    else:
                                        if j != 2:
                                            # *__^*@
                                            if chessboard[i][j - 3] == self.color:
                                                if j != 3:
                                                    # **__^*@
                                                    if chessboard[i][j - 4] == self.color:
                                                        point_self = 1000
                                                    # @*__^*@ or _*__^* or |*__^*
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                            # @__^*@
                                            elif chessboard[i][j - 3] == -self.color:
                                                point_self = 0
                                            # ___^*@
                                            else:
                                                if j != 3:
                                                    # *___^*@
                                                    if chessboard[i][j - 4] == self.color:
                                                        point_self = 100
                                                    # @___^*@ or ____^*@ or |___^*@
                                                    else:
                                                        point_self = 100
                                                else:
                                                    point_self = 100
                                        # |__^*@
                                        else:
                                            point_self = 0
                                # |_^*@
                                else:
                                    point_self = 0
                        # |^*@
                        else:
                            point_self = 0
                    # ^*_
                    else:
                        if j != self.chessboard_size - 3:
                            # ^*_*
                            if chessboard[i][j + 3] == self.color:
                                if j != 0:
                                    # *^*_*
                                    if chessboard[i][j - 1] == self.color:
                                        if j != 1:
                                            # **^*_*
                                            if chessboard[i][j - 2] == self.color:
                                                if j != 2:
                                                    # ***^*_*
                                                    if chessboard[i][j - 3] == self.color:
                                                        if j != 3:
                                                            # ****^*_*
                                                            if chessboard[i][j - 4] == self.color:
                                                                point_self = 1000000
                                                            # @***^*_* or _***^*_* or |***^*_*
                                                            else:
                                                                point_self = 1000000
                                                        else:
                                                            point_self = 1000000
                                                    # @**^*_*
                                                    elif chessboard[i][j - 3] == -self.color:
                                                        point_self = 10000
                                                    # _**^*_*
                                                    else:
                                                        if j != 3:
                                                            # *_**^*_*
                                                            if chessboard[i][j - 4] == self.color:
                                                                point_self = 100000
                                                            # @_**^*_* or __**^*_* or |_**^*_*
                                                            else:
                                                                point_self = 100000
                                                        else:
                                                            point_self = 100000
                                                # |**^*_*
                                                else:
                                                    point_self = 10000
                                            # @*^*_*
                                            elif chessboard[i][j - 2] == -self.color:
                                                if j != self.chessboard_size - 4:
                                                    # @*^*_**
                                                    if chessboard[i][j + 4] == self.color:
                                                        point_self = 0
                                                    # @*^*_*@ or @*^*_*_ or @*^*_*|
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # _*^*_*
                                            else:
                                                if j != 2:
                                                    # *_*^*_*
                                                    if chessboard[i][j - 3] == self.color:
                                                        # **_*^*_**
                                                        if j != self.chessboard_size - 4 \
                                                                and j != 3 \
                                                                and chessboard[i][j - 4] == self.color \
                                                                and chessboard[i][j + 4] == self.color:
                                                            point_self = 100000
                                                        else:
                                                            point_self = 100000
                                                    # @_*^*_* or __*^*_*
                                                    else:
                                                        if j != self.chessboard_size - 4:
                                                            # @_*^*_** or __*^*_**
                                                            if chessboard[i][j + 4] == self.color:
                                                                point_self = 10000
                                                            # @_*^*_*@ or @_*^*_*_ or @_*^*_*| or
                                                            # __*^*_*@ or __*^*_*_ or __*^*_*|
                                                            else:
                                                                point_self = 10000
                                                        else:
                                                            point_self = 10000
                                                # |_*^*_*
                                                else:
                                                    if j != self.chessboard_size - 4:
                                                        # |_*^*_**
                                                        if chessboard[i][j + 4] == self.color:
                                                            point_self = 10000
                                                        # |_*^*_*@ or |_*^*_*_ or |_*^*_*|
                                                        else:
                                                            point_self = 10000
                                                    else:
                                                        point_self = 10000
                                        # |*^*_*
                                        else:
                                            if j != self.chessboard_size - 4:
                                                # |*^*_**
                                                if chessboard[i][j + 4] == self.color:
                                                    point_self = 10000
                                                # |*^*_*@ or |*^*_*_ or |*^*_*|
                                                else:
                                                    point_self = 10000
                                            else:
                                                point_self = 10000
                                    # @^*_*
                                    elif chessboard[i][j - 1] == -self.color:
                                        if j != self.chessboard_size - 4:
                                            # @^*_**
                                            if chessboard[i][j + 4] == self.color:
                                                # @^*_***
                                                if j != self.chessboard_size - 5 and \
                                                        chessboard[i][j + 5] == self.color:
                                                    point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @^*_*@
                                            elif chessboard[i][j + 4] == -self.color:
                                                point_self = 0
                                            # @^*_*_
                                            else:
                                                point_self = 1000
                                        # @^*_*|
                                        else:
                                            point_self = 0
                                    # _^*_*
                                    else:
                                        if j != 1:
                                            # *_^*_*
                                            if chessboard[i][j - 2] == self.color:
                                                point_self = 10000
                                            # @_^*_*
                                            elif chessboard[i][j - 2] == -self.color:
                                                point_self = 1000
                                            # __^*_*
                                            else:
                                                point_self = 1000
                                        # |_^*_*
                                        else:
                                            point_self = 100
                                # |^*_*
                                else:
                                    point_self = 10
                            # ^*_@
                            elif chessboard[i][j + 3] == -self.color:
                                if j != 0:
                                    # *^*_@
                                    if chessboard[i][j - 1] == self.color:
                                        if j != 1:
                                            # **^*_@
                                            if chessboard[i][j - 2] == self.color:
                                                if j != 2:
                                                    # ***^*_@
                                                    if chessboard[i][j - 3] == self.color:
                                                        # ****^*_@
                                                        if j != 3 and \
                                                                chessboard[i][j - 4] == self.color:
                                                            point_self = 1000000
                                                        else:
                                                            point_self = 1000000
                                                    # @**^*_@
                                                    elif chessboard[i][j - 3] == -self.color:
                                                        point_self = 10000
                                                    # _**^*_@
                                                    else:
                                                        point_self = 100000
                                                # |**^*_@
                                                else:
                                                    point_self = 10000
                                            # @*^*_@
                                            elif chessboard[i][j - 2] == -self.color:
                                                point_self = 10000
                                            # _*^*_@
                                            else:
                                                point_self = 10000
                                        # |*^*_@
                                        else:
                                            point_self = 0
                                    # @^*_@
                                    elif chessboard[i][j - 1] == -self.color:
                                        point_self = 0
                                    # _^*_@
                                    else:
                                        point_self = 1000
                                # |^*_@
                                else:
                                    point_self = 0
                            # ^*__
                            else:
                                if j != 0:
                                    # *^*__
                                    if chessboard[i][j - 1] == self.color:
                                        if j != 1:
                                            # **^*__
                                            if chessboard[i][j - 2] == self.color:
                                                if j != 2:
                                                    # ***^*__
                                                    if chessboard[i][j - 3] == self.color:
                                                        if j != 3:
                                                            # ****^*__
                                                            if chessboard[i][j - 4] == self.color:
                                                                point_self = 1000000
                                                            # @***^*_ or _***^*_ or |***^*_
                                                            else:
                                                                point_self = 1000000
                                                        else:
                                                            point_self = 1000000
                                                    # @**^*__
                                                    elif chessboard[i][j - 3] == -self.color:
                                                        point_self = 10000
                                                    # _**^*__
                                                    else:
                                                        point_self = 100000
                                                # |**^*__
                                                else:
                                                    point_self = 10000
                                            # @*^*__
                                            elif chessboard[i][j - 3] == -self.color:
                                                if j != self.chessboard_size - 4:
                                                    # @*^*__*
                                                    if chessboard[i][j + 4] == self.color:
                                                        point_self = 1000
                                                    # @*^*__@ or @*^*___ or @*^*__|
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                            # _*^*__
                                            else:
                                                if j != 2:
                                                    # *_*^*__
                                                    if chessboard[i][j - 3] == self.color:
                                                        if j != 3:
                                                            # **_*^*__
                                                            if chessboard[i][j - 4] == self.color:
                                                                if j != self.chessboard_size - 4:
                                                                    # **_*^*__*
                                                                    if chessboard[i][j + 4] == self.color:
                                                                        point_self = 10000
                                                                    # **_*^*__@ or **_*^*___ or **_*^*__|
                                                                    else:
                                                                        point_self = 1000
                                                                else:
                                                                    point_self = 1000
                                                            # @*_*^*__ or _*_*^*__ or |*_*^*__
                                                            else:
                                                                point_self = 10000
                                                        else:
                                                            point_self = 10000
                                                    # @_*^*__ or  __*^*__  or |_*^*__
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                        # |*^*__
                                        else:
                                            if j != self.chessboard_size - 4:
                                                # |*^*__*
                                                if chessboard[i][j + 4] == self.color:
                                                    point_self = 1000
                                                # |*^*__@ or |*^*___ or |*^*__|
                                                else:
                                                    point_self = 1000
                                            else:
                                                point_self = 1000
                                    # @^*__
                                    elif chessboard[i][j - 1] == -self.color:
                                        point_self = 1
                                    # _^*__
                                    else:
                                        point_self = 1000
                                # |^*__
                                else:
                                    point_self = 1
                        # ^*_|
                        else:
                            if j != 0:
                                # *^*_|
                                if chessboard[i][j - 1] == self.color:
                                    if j != 1:
                                        # **^*_|
                                        if chessboard[i][j - 2] == self.color:
                                            point_self = 100000
                                        # @*^*_|
                                        elif chessboard[i][j - 2] == -self.color:
                                            point_self = 0
                                        # _*^*_|
                                        else:
                                            if j != 2:
                                                # *_*^*_|
                                                if chessboard[i][j - 3] == self.color:
                                                    # **_*^*|
                                                    if j != 3 and \
                                                            chessboard[i][j - 4] == self.color:
                                                        point_self = 10000
                                                    else:
                                                        point_self = 10000
                                                # @_*^*_| or __*^*_| or |_*^*_|
                                                else:
                                                    point_self = 10000
                                            else:
                                                point_self = 10000
                                    # |*^*_|
                                    else:
                                        point_self = 0
                                # @^*_|
                                elif chessboard[i][j - 1] == -self.color:
                                    point_self = 0
                                # _^*_|
                                else:
                                    point_self = 100
                            # |^*_|
                            else:
                                point_self = 0
                # ^*|
                else:
                    if j != 0:
                        # *^*|
                        if chessboard[i][j - 1] == self.color:
                            if j != 1:
                                # **^*|
                                if chessboard[i][j - 2] == self.color:
                                    if j != 2:
                                        # ***^*|
                                        if chessboard[i][j - 3] == self.color:
                                            # ****^*|
                                            if j != 3 and \
                                                    chessboard[i][j - 4] == self.color:
                                                point_self = 1000000
                                            else:
                                                point_self = 1000000
                                        # @**^*|
                                        elif chessboard[i][j - 3] == -self.color:
                                            point_self = 1
                                        # _**^*|
                                        else:
                                            # *_**^*|
                                            if j != 3 and \
                                                    chessboard[i][j - 4] == self.color:
                                                point_self = 10000
                                            else:
                                                point_self = 10000
                                    # |**^*|
                                    else:
                                        point_self = 0
                                # @*^*|
                                elif chessboard[i][j - 2] == -self.color:
                                    point_self = 0
                                # _*^*|
                                else:
                                    if j != 2:
                                        # *_*^*|
                                        if chessboard[i][j - 3] == self.color:
                                            point_self = 10000
                                        # @_*^*|
                                        elif chessboard[i][j - 3] == -self.color:
                                            point_self = 0
                                        # __*^*|
                                        else:
                                            # *__*^*|
                                            if j != 3 and \
                                                    chessboard[i][j - 4] == self.color:
                                                point_self = 1000
                                            else:
                                                point_self = 1000
                                    # |_*^*|
                                    else:
                                        point_self = 0
                            # |*^*|
                            else:
                                point_self = 0
                        # @^*|
                        elif chessboard[i][j - 1] == -self.color:
                            point_self = 0
                        # _^*|
                        else:
                            if j != 1:
                                # *_^*|
                                if chessboard[i][j - 2] == self.color:
                                    if j != 2:
                                        # **_^*|
                                        if chessboard[i][j - 3] == self.color:
                                            # ***_^*|
                                            if j != 3 and \
                                                    chessboard[i][j - 4] == self.color:
                                                point_self = 10000
                                            else:
                                                point_self = 10000
                                        # @*_^*|
                                        elif chessboard[i][j - 3] == -self.color:
                                            point_self = 10
                                        # _*_^*|
                                        else:
                                            # *_*_^*|
                                            if j != 3 and \
                                                    chessboard[i][j - 4] == self.color:
                                                point_self = 100
                                            else:
                                                point_self = 100
                                    # |*_^*|
                                    else:
                                        point_self = 0
                                # @_^*|
                                elif chessboard[i][j - 2] == -self.color:
                                    point_self = 0
                                # __^*|
                                else:
                                    if j != 2:
                                        #  *__^*|
                                        if chessboard[i][j - 3] == self.color:
                                            # **__^*|
                                            if j != 3 and \
                                                    chessboard[i][j - 4] == self.color:
                                                point_self = 100
                                            else:
                                                point_self = 100
                                        # @__^*|
                                        elif chessboard[i][j - 3] == -self.color:
                                            point_self = 0
                                        # ___^*|
                                        else:
                                            # *___^*|
                                            if j != 3 and \
                                                    chessboard[i][j - 4] == self.color:
                                                point_self = 100
                                            else:
                                                point_self = 100
                                    # |__^*|
                                    else:
                                        point_self = 0
                            # |_^*|
                            else:
                                point_self = 0
                    # |^*|
                    else:
                        point_self = 0
            # ^@
            elif chessboard[i][j + 1] == -self.color:
                if j != 0:
                    # *^@
                    if chessboard[i][j - 1] == self.color:
                        if j != 1:
                            # **^@
                            if chessboard[i][j - 2] == self.color:
                                if j != 2:
                                    # ***^@
                                    if chessboard[i][j - 3] == self.color:
                                        if j != 3:
                                            # ****^@
                                            if chessboard[i][j - 4] == self.color:
                                                point_self = 1000000
                                            # @***^@
                                            elif chessboard[i][j - 4] == -self.color:
                                                point_self = 0
                                            # _***^@
                                            else:
                                                # *_***^@
                                                if j != 4 and \
                                                        chessboard[i][j - 5] == self.color:
                                                    point_self = 10000
                                                else:
                                                    point_self = 10000
                                        # |***^@
                                        else:
                                            point_self = 0
                                    # @**^@
                                    elif chessboard[i][j - 3] == -self.color:
                                        point_self = 0
                                    # _**^@
                                    else:
                                        point_self = 1000
                                # |**^@
                                else:
                                    point_self = 0
                            # @*^@
                            elif chessboard[i][j - 2] == -self.color:
                                point_self = 0
                            # _*^@
                            else:
                                if j != 2:
                                    # *_*^@
                                    if chessboard[i][j - 3] == self.color:
                                        point_self = 100
                                    # @_*^@
                                    elif chessboard[i][j - 3] == -self.color:
                                        point_self = 0
                                    # __*^@
                                    else:
                                        point_self = 1
                                # |_*^@
                                else:
                                    point_self = 0
                        # |*^@
                        else:
                            point_self = 0
                    # @^@
                    elif chessboard[i][j - 1] == -self.color:
                        point_self = 0
                    # _^@
                    else:
                        if j != 1:
                            # *_^@
                            if chessboard[i][j - 2] == self.color:
                                point_self = 10
                            # @_^@
                            elif chessboard[i][j - 2] == -self.color:
                                point_self = 0
                            # __^@
                            else:
                                point_self = 1
                        # |_^@
                        else:
                            point_self = 0
                # |^@
                else:
                    point_self = 0
            # ^_
            else:
                if j != self.chessboard_size - 2:
                    # ^_*
                    if chessboard[i][j + 2] == self.color:
                        if j != 0:
                            # *^_*
                            if chessboard[i][j - 1] == self.color:
                                if j != 1:
                                    # **^_*
                                    if chessboard[i][j - 2] == self.color:
                                        if j != 2:
                                            # ***^_*
                                            if chessboard[i][j - 3] == self.color:
                                                if j != 3:
                                                    # ****^_*
                                                    if chessboard[i][j - 4] == self.color:
                                                        point_self = 1000000
                                                    # @***^_*
                                                    elif chessboard[i][j - 4] == self.color:
                                                        point_self = 10000
                                                    # _***^_*
                                                    else:
                                                        # *_***^_*
                                                        if j != 4 and \
                                                                chessboard[i][j - 5] == self.color:
                                                            point_self = 100000
                                                        else:
                                                            point_self = 100000
                                                # |***^_*
                                                else:
                                                    point_self = 10000
                                            # @**^_*
                                            elif chessboard[i][j - 3] == -self.color:
                                                # @**^_**
                                                if j != self.chessboard_size - 3 and \
                                                        chessboard[i][j + 3] == self.color:
                                                    point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # _**^_*
                                            else:
                                                point_self = 10000
                                        # |**^_*
                                        else:
                                            point_self = 10000
                                    # @*^_*
                                    elif chessboard[i][j - 2] == -self.color:
                                        point_self = 10
                                    # _*^_*
                                    else:
                                        point_self = 10000
                                # |*^_*
                                else:
                                    point_self = 10
                            # @^_*
                            elif chessboard[i][j - 1] == -self.color:
                                point_self = 1
                            # _^_*
                            else:
                                point_self = 1
                        # |^_*
                        else:
                            point_self = 0
                    # ^_@
                    elif chessboard[i][j + 2] == -self.color:
                        if j != 0:
                            # *^_@
                            if chessboard[i][j - 1] == self.color:
                                if j != 1:
                                    # **^_@
                                    if chessboard[i][j - 2] == self.color:
                                        if j != 2:
                                            # ***^_@
                                            if chessboard[i][j - 3] == self.color:
                                                if j != 3:
                                                    # ****^_@
                                                    if chessboard[i][j - 4] == self.color:
                                                        point_self = 1000000
                                                    # @***^_@
                                                    elif chessboard[i][j - 4] == -self.color:
                                                        point_self = 10000
                                                    # _***^_@
                                                    else:
                                                        point_self = 100000
                                                # |***^_@
                                                else:
                                                    point_self = 10000
                                            # @**^_@
                                            elif chessboard[i][j - 3] == -self.color:
                                                point_self = 0
                                            # _**^_@
                                            else:
                                                point_self = 10000
                                        # |**^_@
                                        else:
                                            point_self = 1
                                    # @*^_@
                                    elif chessboard[i][j - 2] == -self.color:
                                        point_self = 1
                                    # _*^_@
                                    else:
                                        point_self = 1
                                # |*^_@
                                else:
                                    point_self = 1
                            # @^_@
                            elif chessboard[i][j - 1] == -self.color:
                                point_self = 1
                            # _^_@
                            else:
                                point_self = 1
                        # |^_@
                        else:
                            point_self = 1
                    # ^__
                    else:
                        if j != 0:
                            # *^__
                            if chessboard[i][j - 1] == self.color:
                                if j != 1:
                                    # **^__
                                    if chessboard[i][j - 2] == self.color:
                                        if j != 2:
                                            # ***^__
                                            if chessboard[i][j - 3] == self.color:
                                                if j != 3:
                                                    # ****^__
                                                    if chessboard[i][j - 4] == self.color:
                                                        point_self = 1000000
                                                    # @***^__
                                                    elif chessboard[i][j - 4] == -self.color:
                                                        point_self = 10000
                                                    # _***^__
                                                    else:
                                                        point_self = 100000
                                                # |***^__
                                                else:
                                                    point_self = 10000
                                            # @**^__
                                            elif chessboard[i][j - 3] == -self.color:
                                                point_self = 100
                                            # _**^__
                                            else:
                                                point_self = 10000
                                        # |**^__
                                        else:
                                            point_self = 100
                                    # @*^__
                                    elif chessboard[i][j - 2] == -self.color:
                                        point_self = 50
                                    # _*^__
                                    else:
                                        if j != 2:
                                            # *_*^__
                                            if chessboard[i][j - 3] == self.color:
                                                point_self = 100
                                            # @_*^__
                                            elif chessboard[i][j - 3] == -self.color:
                                                point_self = 100
                                            # __*^__
                                            else:
                                                point_self = 100
                                        # |_*^__
                                        else:
                                            point_self = 100
                                # |*^__
                                else:
                                    point_self = 1
                            # @^__
                            elif chessboard[i][j - 1] == -self.color:
                                point_self = 1
                            # _^__
                            else:
                                point_self = 1
                        # |^__
                        else:
                            point_self = 0
                # ^_|
                else:
                    if j != 0:
                        # *^_|
                        if chessboard[i][j - 1] == self.color:
                            if j != 1:
                                # **^_|
                                if chessboard[i][j - 2] == self.color:
                                    if j != 2:
                                        # ***^_|
                                        if chessboard[i][j - 3] == self.color:
                                            if j != 3:
                                                # ****^_|
                                                if chessboard[i][j - 4] == self.color:
                                                    point_self = 1000000
                                                # @***^_|
                                                elif chessboard[i][j - 4] == -self.color:
                                                    point_self = 10000
                                                # _***^_|
                                                else:
                                                    point_self = 100000
                                            # |***^_|
                                            else:
                                                point_self = 10000
                                        # @**^_|
                                        elif chessboard[i][j - 3] == -self.color:
                                            point_self = 1
                                        # _**^_|
                                        else:
                                            point_self = 10000
                                    # |**^_|
                                    else:
                                        point_self = 0
                                # @*^_|
                                elif chessboard[i][j - 2] == -self.color:
                                    point_self = 0
                                # _*^_|
                                else:
                                    # *_*^_|
                                    if j != 2 and \
                                            chessboard[i][j - 3] == self.color:
                                        point_self = 1000
                                    else:
                                        point_self = 1000
                            # |*^_|
                            else:
                                point_self = 0
                        # @^_|
                        elif chessboard[i][j - 1] == -self.color:
                            point_self = 0
                        # _^_|
                        else:
                            point_self = 0
                    # |^_|
                    else:
                        point_self = 0
        # ^|
        else:
            if j != 0:
                # *^|
                if chessboard[i][j - 1] == self.color:
                    if j != 1:
                        # **^|
                        if chessboard[i][j - 2] == self.color:
                            if j != 2:
                                # ***^|
                                if chessboard[i][j - 3] == self.color:
                                    if j != 3:
                                        # ****^|
                                        if chessboard[i][j - 4] == self.color:
                                            point_self = 1000000
                                        # @***^|
                                        elif chessboard[i][j - 4] == -self.color:
                                            point_self = 1
                                        # _***^|
                                        else:
                                            # *_***^|
                                            if j != 4 and \
                                                    chessboard[i][j - 5] == self.color:
                                                point_self = 10000
                                            else:
                                                point_self = 10000
                                    # |***^|
                                    else:
                                        point_self = 0
                                # @**^|
                                elif chessboard[i][j - 3] == -self.color:
                                    point_self = 0
                                # _**^|
                                else:
                                    point_self = 0
                            # |**^|
                            else:
                                point_self = 0
                        # @*^|
                        elif chessboard[i][j - 2] == -self.color:
                            point_self = 0
                        # _*^|
                        else:
                            point_self = 1
                    # |*^|
                    else:
                        point_self = 0
                # @^|
                elif chessboard[i][j - 1] == -self.color:
                    point_self = 0
                # _^|
                else:
                    point_self = 1
            # |^|
            else:
                point_self = 0
        return point_self

    def checkPie(self, i, j, chessboard):
        if i != self.chessboard_size - 1 and j != 0:
            # ^*
            if chessboard[i + 1][j - 1] == self.color:
                if i != self.chessboard_size - 2 and j != 1:
                    # ^**
                    if chessboard[i + 2][j - 2] == self.color:
                        if i != self.chessboard_size - 3 and j != 2:
                            # ^***
                            if chessboard[i + 3][j - 3] == self.color:
                                if i != self.chessboard_size - 4 and j != 3:
                                    # ^****
                                    if chessboard[i + 4][j - 4] == self.color:
                                        point_self = 1000000
                                    # ^***@
                                    elif chessboard[i + 4][j - 4] == -self.color:
                                        if i != 0 and j != self.chessboard_size - 1:
                                            # *^***@
                                            if chessboard[i - 1][j + 1] == self.color:
                                                point_self = 1000000
                                            # @^***@
                                            elif chessboard[i - 1][j + 1] == -self.color:
                                                point_self = 10
                                            # _^***@
                                            else:
                                                if i != 1 and j != self.chessboard_size - 2:
                                                    # *_^***@
                                                    if chessboard[i - 2][j + 2] == self.color:
                                                        point_self = 0
                                                    # @_^***@ or __^***@ or |_^***@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                        # |^***@
                                        else:
                                            point_self = 10
                                    # ^***_
                                    else:
                                        if i != 0 and j != self.chessboard_size - 1:
                                            # *^***_
                                            if chessboard[i - 1][j + 1] == self.color:
                                                if i != 1 and j != self.chessboard_size - 2:
                                                    # **^***_
                                                    if chessboard[i - 2][j + 2] == self.color:
                                                        point_self = 0
                                                    # @*^***_ or _*^***_ or |*^***_
                                                    else:
                                                        point_self = 1000000
                                                else:
                                                    point_self = 1000000
                                            # @^***_
                                            elif chessboard[i - 1][j + 1] == -self.color:
                                                point_self = 10000
                                            # _^***_
                                            else:
                                                point_self = 100000
                                        # |^***_
                                        else:
                                            point_self = 10000
                                # ^***|
                                else:
                                    if i != 0 and j != self.chessboard_size - 1:
                                        # *^***|
                                        if chessboard[i - 1][j + 1] == self.color:
                                            point_self = 1000000
                                        # @^***|
                                        elif chessboard[i - 1][j + 1] == -self.color:
                                            point_self = 1000000
                                        # _^***|
                                        else:
                                            point_self = 10000
                                    # |^***|
                                    else:
                                        point_self = 0
                            # ^**@
                            elif chessboard[i + 3][j - 3] == -self.color:
                                if i != 0 and j != self.chessboard_size - 1:
                                    # *^**@
                                    if chessboard[i - 1][j + 1] == self.color:
                                        if i != 1 and j != self.chessboard_size - 2:
                                            # **^**@
                                            if chessboard[i - 2][j + 2] == self.color:
                                                point_self = 1000000
                                            # @*^**@
                                            elif chessboard[i - 2][j + 2] == -self.color:
                                                point_self = 0
                                            # _*^**@
                                            else:
                                                point_self = 10000
                                        # |^**@
                                        else:
                                            point_self = 0
                                    # @^**@
                                    elif chessboard[i - 1][j + 1] == -self.color:
                                        point_self = 0
                                    # _^**@
                                    else:
                                        if i != 1 and j != self.chessboard_size - 2:
                                            # *_^**@
                                            if chessboard[i - 2][j + 2] == self.color:
                                                if i != 2 and j != self.chessboard_size - 3:
                                                    # **_^**@
                                                    if chessboard[i - 3][j + 3] == self.color:
                                                        point_self = 10000
                                                    # @*_^**@ or _*_^**@ or |*_^**@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @_^**@
                                            elif chessboard[i - 2][j + 2] == -self.color:
                                                point_self = 0
                                            # __^**@
                                            else:
                                                if i != 2 and j != self.chessboard_size - 3:
                                                    # *__^**@
                                                    if chessboard[i - 3][j + 3] == self.color:
                                                        point_self = 1000
                                                    # @__^**@ or ___^**@ or |__^**@
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                        # |_^**@
                                        else:
                                            point_self = 0
                                # |^**@
                                else:
                                    point_self = 0
                            # ^**_
                            else:
                                if i != 0 and j != self.chessboard_size - 1:
                                    # *^**_
                                    if chessboard[i - 1][j + 1] == self.color:
                                        if i != 1 and j != self.chessboard_size - 2:
                                            # **^**_
                                            if chessboard[i - 2][j + 2] == self.color:
                                                if i != 2 and j != self.chessboard_size - 3:
                                                    # ***^**_
                                                    if chessboard[i - 3][j + 3] == self.color:
                                                        point_self = 1000000
                                                    # @**^**_ or _**^**_ or |**^**_
                                                    else:
                                                        point_self = 1000000
                                                else:
                                                    point_self = 1000000
                                            # @*^**_
                                            elif chessboard[i - 2][j + 2] == -self.color:
                                                if i != self.chessboard_size - 4 and j != 3:
                                                    # @*^**_*
                                                    if chessboard[i + 4][j - 4] == self.color:
                                                        point_self = 10000
                                                    # @*^**_@ or @*^**__ or @*^**_|
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # _*^**_
                                            else:
                                                if i != 1 and j != self.chessboard_size - 2:
                                                    # *_^**_
                                                    if chessboard[i - 2][j + 2] == self.color:
                                                        point_self = 10000
                                                    # @_^**_
                                                    elif chessboard[i - 2][j + 2] == -self.color:
                                                        point_self = 10000
                                                    # __^**_
                                                    else:
                                                        if i != 2 and j != self.chessboard_size - 3:
                                                            # *__^**_
                                                            if chessboard[i - 3][j + 3] == self.color:
                                                                point_self = 10000
                                                            # @__^**_
                                                            elif chessboard[i - 3][j + 3] == -self.color:
                                                                point_self = 10000
                                                            # ___^**_
                                                            else:
                                                                point_self = 10000
                                                        # |__^**_
                                                        else:
                                                            point_self = 10000
                                                # |_^**_
                                                else:
                                                    point_self = 100
                                        # |*^**_
                                        else:
                                            point_self = 10000
                                    # @^**_
                                    elif chessboard[i - 1][j + 1] == -self.color:
                                        point_self = 100
                                    # _^**_
                                    else:
                                        point_self = 10000
                                # |^**_
                                else:
                                    point_self = 100
                        # ^**|
                        else:
                            if i != 0 and j != self.chessboard_size - 1:
                                # *^**|
                                if chessboard[i - 1][j + 1] == self.color:
                                    if i != 1 and j != self.chessboard_size - 2:
                                        # **^**|
                                        if chessboard[i - 2][j + 2] == self.color:
                                            point_self = 1000000
                                        # @*^**|
                                        elif chessboard[i - 2][j + 2] == -self.color:
                                            point_self = 0
                                        # _*^**|
                                        else:
                                            point_self = 10000
                                    # |*^**|
                                    else:
                                        point_self = 0
                                # @^**|
                                elif chessboard[i - 1][j + 1] == -self.color:
                                    point_self = 0
                                # _^**|
                                else:
                                    if i != 1 and j != self.chessboard_size - 2:
                                        # *_^**|
                                        if chessboard[i - 2][j + 2] == self.color:
                                            point_self = 10000
                                        # @_^**|
                                        elif chessboard[i - 2][j + 2] == -self.color:
                                            point_self = 0
                                        # __^**|
                                        else:
                                            point_self = 100
                                    # |_^**|
                                    else:
                                        point_self = 0
                            # |^**|
                            else:
                                point_self = 0
                    # ^*@
                    elif chessboard[i + 2][j - 2] == -self.color:
                        if i != 0 and j != self.chessboard_size - 1:
                            # *^*@
                            if chessboard[i - 1][j + 1] == self.color:
                                if i != 1 and j != self.chessboard_size - 2:
                                    # **^*@
                                    if chessboard[i - 2][j + 2] == self.color:
                                        if i != 2 and j != self.chessboard_size - 3:
                                            # ***^*@
                                            if chessboard[i - 3][j + 3] == self.color:
                                                point_self = 1000000
                                            # @**^*@
                                            elif chessboard[i - 3][j + 3] == -self.color:
                                                point_self = 0
                                            # _**^*@
                                            else:
                                                point_self = 10000
                                        # |**^*@
                                        else:
                                            point_self = 0
                                    # @*^*@
                                    elif chessboard[i - 2][j + 2] == -self.color:
                                        point_self = 0
                                    # _*^*@
                                    else:
                                        if i != 2 and j != self.chessboard_size - 3:
                                            # *_*^*@
                                            if chessboard[i - 3][j + 3] == self.color:
                                                if i != 3 and j != self.chessboard_size - 4:
                                                    # **_*^*@
                                                    if chessboard[i - 4][j + 4] == self.color:
                                                        point_self = 0
                                                    # @*_*^*@ or _*_*^*@ or |*_*^*@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @_*^*@
                                            elif chessboard[i - 3][j + 3] == -self.color:
                                                point_self = 0
                                            # __*^*@
                                            else:
                                                if i != 3 and j != self.chessboard_size - 4:
                                                    # *__*^*@
                                                    if chessboard[i - 4][j + 4] == self.color:
                                                        point_self = 0
                                                    # @__*^*@ or ___*^*@ or |__*^*@
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                        # |_*^*@
                                        else:
                                            point_self = 0
                                # |*^*@
                                else:
                                    point_self = 0
                            # @^*@
                            elif chessboard[i - 1][j + 1] == -self.color:
                                point_self = 0
                            # _^*@
                            else:
                                if i != 1 and j != self.chessboard_size - 2:
                                    # *_^*@
                                    if chessboard[i - 2][j + 2] == self.color:
                                        if i != 2 and j != self.chessboard_size - 3:
                                            # **_^*@
                                            if chessboard[i - 3][j + 3] == self.color:
                                                if i != 3 and j != self.chessboard_size - 4:
                                                    # ***_^*@
                                                    if chessboard[i - 4][j + 4] == self.color:
                                                        point_self = 0
                                                    # @**_^*@ or _**_^*@ or |**_^*@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @*_^*@
                                            elif chessboard[i - 3][j + 3] == -self.color:
                                                point_self = 0
                                            # _*_^*@
                                            else:
                                                if i != 3 and j != self.chessboard_size - 4:
                                                    # *_*_^*@
                                                    if chessboard[i - 4][j + 4] == self.color:
                                                        point_self = 0
                                                    # @_*_^*@ or __*_^*@ or |_*_^*@
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                        # |*_^*@
                                        else:
                                            point_self = 0
                                    # @_^*@
                                    elif chessboard[i - 2][j + 2] == -self.color:
                                        point_self = 0
                                    # __^*@
                                    else:
                                        if i != 2 and j != self.chessboard_size - 3:
                                            # *__^*@
                                            if chessboard[i - 3][j + 3] == self.color:
                                                if i != 3 and j != self.chessboard_size - 4:
                                                    # **__^*@
                                                    if chessboard[i - 4][j + 4] == self.color:
                                                        point_self = 0
                                                    # @*__^*@ or _*__^* or |*__^*
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                            # @__^*@
                                            elif chessboard[i - 3][j + 3] == -self.color:
                                                point_self = 0
                                            # ___^*@
                                            else:
                                                if i != 3 and j != self.chessboard_size - 4:
                                                    # *___^*@
                                                    if chessboard[i - 4][j + 4] == self.color:
                                                        point_self = 0
                                                    # @___^*@ or ____^*@ or |___^*@
                                                    else:
                                                        point_self = 10
                                                else:
                                                    point_self = 10
                                        # |__^*@
                                        else:
                                            point_self = 0
                                # |_^*@
                                else:
                                    point_self = 0
                        # |^*@
                        else:
                            point_self = 0
                    # ^*_
                    else:
                        if i != self.chessboard_size - 3 and j != 2:
                            # ^*_*
                            if chessboard[i + 3][j - 3] == self.color:
                                if i != 0 and j != self.chessboard_size - 1:
                                    # *^*_*
                                    if chessboard[i - 1][j + 1] == self.color:
                                        if i != 1 and j != self.chessboard_size - 2:
                                            # **^*_*
                                            if chessboard[i - 2][j + 2] == self.color:
                                                if i != 2 and j != self.chessboard_size - 3:
                                                    # ***^*_*
                                                    if chessboard[i - 3][j + 3] == self.color:
                                                        if i != 3 and j != self.chessboard_size - 4:
                                                            # ****^*_*
                                                            if chessboard[i - 4][j + 4] == self.color:
                                                                point_self = 0
                                                            # @***^*_* or _***^*_* or |***^*_*
                                                            else:
                                                                point_self = 1000000
                                                        else:
                                                            point_self = 1000000
                                                    # @**^*_*
                                                    elif chessboard[i - 3][j + 3] == -self.color:
                                                        point_self = 0
                                                    # _**^*_*
                                                    else:
                                                        if i != 3 and j != self.chessboard_size - 4:
                                                            # *_**^*_*
                                                            if chessboard[i - 4][j + 4] == self.color:
                                                                point_self = 0
                                                            # @_**^*_* or __**^*_* or |_**^*_*
                                                            else:
                                                                point_self = 100000
                                                        else:
                                                            point_self = 100000
                                                # |**^*_*
                                                else:
                                                    point_self = 0
                                            # @*^*_*
                                            elif chessboard[i - 2][j + 2] == -self.color:
                                                if i != self.chessboard_size - 4 and j != 3:
                                                    # @*^*_**
                                                    if chessboard[i + 4][j - 4] == self.color:
                                                        point_self = 0
                                                    # @*^*_*@ or @*^*_*_ or @*^*_*|
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # _*^*_*
                                            else:
                                                if i != 2 and j != self.chessboard_size - 3:
                                                    # *_*^*_*
                                                    if chessboard[i - 3][j + 3] == self.color:
                                                        # **_*^*_**
                                                        if i != self.chessboard_size - 4 and j != 3 \
                                                                and i != 3 and j != self.chessboard_size - 4 \
                                                                and chessboard[i - 4][j + 4] == self.color \
                                                                and chessboard[i + 4][j - 4] == self.color:
                                                            point_self = 0
                                                        else:
                                                            point_self = 10000
                                                    # @_*^*_* or __*^*_*
                                                    else:
                                                        if i != self.chessboard_size - 4 and j != 3:
                                                            # @_*^*_** or __*^*_**
                                                            if chessboard[i + 4][j - 4] == self.color:
                                                                point_self = 0
                                                            # @_*^*_*@ or @_*^*_*_ or @_*^*_*| or
                                                            # __*^*_*@ or __*^*_*_ or __*^*_*|
                                                            else:
                                                                point_self = 10000
                                                        else:
                                                            point_self = 10000
                                                # |_*^*_*
                                                else:
                                                    if i != self.chessboard_size - 4 and j != 3:
                                                        # |_*^*_**
                                                        if chessboard[i + 4][j - 4] == self.color:
                                                            point_self = 0
                                                        # |_*^*_*@ or |_*^*_*_ or |_*^*_*|
                                                        else:
                                                            point_self = 10000
                                                    else:
                                                        point_self = 10000
                                        # |*^*_*
                                        else:
                                            if i != self.chessboard_size - 4 and j != 3:
                                                # |*^*_**
                                                if chessboard[i + 4][j - 4] == self.color:
                                                    point_self = 0
                                                # |*^*_*@ or |*^*_*_ or |*^*_*|
                                                else:
                                                    point_self = 10000
                                            else:
                                                point_self = 10000
                                    # @^*_*
                                    elif chessboard[i - 1][j + 1] == -self.color:
                                        if i != self.chessboard_size - 4 and j != 3:
                                            # @^*_**
                                            if chessboard[i + 4][j - 4] == self.color:
                                                # @^*_***
                                                if i != self.chessboard_size - 5 and j != 4 and \
                                                        chessboard[i + 5][j - 5] == self.color:
                                                    point_self = 0
                                                else:
                                                    point_self = 10000
                                            # @^*_*@
                                            elif chessboard[i + 4][j - 4] == -self.color:
                                                point_self = 0
                                            # @^*_*_
                                            else:
                                                point_self = 100
                                        # @^*_*|
                                        else:
                                            point_self = 0
                                    # _^*_*
                                    else:
                                        if i != 1 and j != self.chessboard_size - 2:
                                            # *_^*_*
                                            if chessboard[i - 2][j + 2] == self.color:
                                                point_self = 10000
                                            # @_^*_*
                                            elif chessboard[i - 2][j + 2] == -self.color:
                                                point_self = 100
                                            # __^*_*
                                            else:
                                                point_self = 100
                                        # |_^*_*
                                        else:
                                            point_self = 100
                                # |^*_*
                                else:
                                    point_self = 10
                            # ^*_@
                            elif chessboard[i + 3][j - 3] == -self.color:
                                if i != 0 and j != self.chessboard_size - 1:
                                    # *^*_@
                                    if chessboard[i - 1][j + 1] == self.color:
                                        if i != 1 and j != self.chessboard_size - 2:
                                            # **^*_@
                                            if chessboard[i - 2][j + 2] == self.color:
                                                if i != 2 and j != self.chessboard_size - 3:
                                                    # ***^*_@
                                                    if chessboard[i - 3][j + 3] == self.color:
                                                        # ****^*_@
                                                        if i != 3 and j != self.chessboard_size - 4 and \
                                                                chessboard[i - 4][j + 4] == self.color:
                                                            point_self = 0
                                                        else:
                                                            point_self = 1000000
                                                    # @**^*_@
                                                    elif chessboard[i - 3][j + 3] == -self.color:
                                                        point_self = 10000
                                                    # _**^*_@
                                                    else:
                                                        point_self = 100000
                                                # |**^*_@
                                                else:
                                                    point_self = 10000
                                            # @*^*_@
                                            elif chessboard[i - 2][j + 2] == -self.color:
                                                point_self = 0
                                            # _*^*_@
                                            else:
                                                point_self = 10000
                                        # |*^*_@
                                        else:
                                            point_self = 0
                                    # @^*_@
                                    elif chessboard[i - 1][j + 1] == -self.color:
                                        point_self = 1
                                    # _^*_@
                                    else:
                                        point_self = 1000
                                # |^*_@
                                else:
                                    point_self = 1
                            # ^*__
                            else:
                                if i != 0 and j != self.chessboard_size - 1:
                                    # *^*__
                                    if chessboard[i - 1][j + 1] == self.color:
                                        if i != 1 and j != self.chessboard_size - 2:
                                            # **^*__
                                            if chessboard[i - 2][j + 2] == self.color:
                                                if i != 2 and j != self.chessboard_size - 3:
                                                    # ***^*__
                                                    if chessboard[i - 3][j + 3] == self.color:
                                                        if i != 3 and j != self.chessboard_size - 4:
                                                            # ****^*__
                                                            if chessboard[i - 4][j + 4] == self.color:
                                                                point_self = 0
                                                            # @***^*_ or _***^*_ or |***^*_
                                                            else:
                                                                point_self = 1000000
                                                        else:
                                                            point_self = 1000000
                                                    # @**^*__
                                                    elif chessboard[i - 3][j + 3] == -self.color:
                                                        point_self = 10000
                                                    # _**^*__
                                                    else:
                                                        point_self = 100000
                                                # |**^*__
                                                else:
                                                    point_self = 10000
                                            # @*^*__
                                            elif chessboard[i - 3][j + 3] == -self.color:
                                                if i != self.chessboard_size - 4 and j != 3:
                                                    # @*^*__*
                                                    if chessboard[i + 4][j - 4] == self.color:
                                                        point_self = 0
                                                    # @*^*__@ or @*^*___ or @*^*__|
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                            # _*^*__
                                            else:
                                                if i != 2 and j != self.chessboard_size - 3:
                                                    # *_*^*__
                                                    if chessboard[i - 3][j + 3] == self.color:
                                                        if i != 3 and j != self.chessboard_size - 4:
                                                            # **_*^*__
                                                            if chessboard[i - 4][j + 4] == self.color:
                                                                if i != self.chessboard_size - 4 and j != 3:
                                                                    # **_*^*__*
                                                                    if chessboard[i + 4][j - 4] == self.color:
                                                                        point_self = 0
                                                                    # **_*^*__@ or **_*^*___ or **_*^*__|
                                                                    else:
                                                                        point_self = 1000
                                                                else:
                                                                    point_self = 1000
                                                            # @*_*^*__ or _*_*^*__ or |*_*^*__
                                                            else:
                                                                point_self = 10000
                                                        else:
                                                            point_self = 10000
                                                    # @_*^*__ or  __*^*__  or |_*^*__
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000

                                        # |*^*__
                                        else:
                                            if i != self.chessboard_size - 4 and j != 3:
                                                # |*^*__*
                                                if chessboard[i + 4][j - 4] == self.color:
                                                    point_self = 0
                                                # |*^*__@ or |*^*___ or |*^*__|
                                                else:
                                                    point_self = 1000
                                            else:
                                                point_self = 1000
                                    # @^*__
                                    elif chessboard[i - 1][j + 1] == -self.color:
                                        point_self = 1
                                    # _^*__
                                    else:
                                        point_self = 1000
                                # |^*__
                                else:
                                    point_self = 1
                        # ^*_|
                        else:
                            if i != 0 and j != self.chessboard_size - 1:
                                # *^*_|
                                if chessboard[i - 1][j + 1] == self.color:
                                    if i != 1 and j != self.chessboard_size - 2:
                                        # **^*_|
                                        if chessboard[i - 2][j + 2] == self.color:
                                            point_self = 100000
                                        # @*^*_|
                                        elif chessboard[i - 2][j + 2] == -self.color:
                                            point_self = 0
                                        # _*^*_|
                                        else:
                                            if i != 2 and j != self.chessboard_size - 3:
                                                # *_*^*_|
                                                if chessboard[i - 3][j + 3] == self.color:
                                                    # **_*^*|
                                                    if i != 3 and j != self.chessboard_size - 4 and \
                                                            chessboard[i - 4][j + 4] == self.color:
                                                        point_self = 0
                                                    else:
                                                        point_self = 10000
                                                # @_*^*_| or __*^*_| or |_*^*_|
                                                else:
                                                    point_self = 10000
                                            else:
                                                point_self = 10000
                                    # |*^*_|
                                    else:
                                        point_self = 0
                                # @^*_|
                                elif chessboard[i - 1][j + 1] == -self.color:
                                    point_self = 0
                                # _^*_|
                                else:
                                    point_self = 100
                            # |^*_|
                            else:
                                point_self = 0
                # ^*|
                else:
                    if i != 0 and j != self.chessboard_size - 1:
                        # *^*|
                        if chessboard[i - 1][j + 1] == self.color:
                            if i != 1 and j != self.chessboard_size - 2:
                                # **^*|
                                if chessboard[i - 2][j + 2] == self.color:
                                    if i != 2 and j != self.chessboard_size - 3:
                                        # ***^*|
                                        if chessboard[i - 3][j + 3] == self.color:
                                            # ****^*|
                                            if i != 3 and j != self.chessboard_size - 4 and \
                                                    chessboard[i - 4][j + 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 1000000
                                        # @**^*|
                                        elif chessboard[i - 3][j + 3] == -self.color:
                                            point_self = 1
                                        # _**^*|
                                        else:
                                            # *_**^*|
                                            if i != 3 and j != self.chessboard_size - 4 and \
                                                    chessboard[i - 4][j + 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 10000
                                    # |**^*|
                                    else:
                                        point_self = 0
                                # @*^*|
                                elif chessboard[i - 2][j + 2] == -self.color:
                                    point_self = 0
                                # _*^*|
                                else:
                                    if i != 2 and j != self.chessboard_size - 3:
                                        # *_*^*|
                                        if chessboard[i - 3][j + 3] == self.color:
                                            point_self = 10000
                                        # @_*^*|
                                        elif chessboard[i - 3][j + 3] == -self.color:
                                            point_self = 0
                                        # __*^*|
                                        else:
                                            # *__*^*|
                                            if i != 3 and j != self.chessboard_size - 4 and \
                                                    chessboard[i - 4][j + 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 1000
                                    # |_*^*|
                                    else:
                                        point_self = 0
                            # |*^*|
                            else:
                                point_self = 0
                        # @^*|
                        elif chessboard[i - 1][j + 1] == -self.color:
                            point_self = 0
                        # _^*|
                        else:
                            if i != 1 and j != self.chessboard_size - 2:
                                # *_^*|
                                if chessboard[i - 2][j + 2] == self.color:
                                    if i != 2 and j != self.chessboard_size - 3:
                                        # **_^*|
                                        if chessboard[i - 3][j + 3] == self.color:
                                            # ***_^*|
                                            if i != 3 and j != self.chessboard_size - 4 and \
                                                    chessboard[i - 4][j + 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 10000
                                        # @*_^*|
                                        elif chessboard[i - 3][j + 3] == -self.color:
                                            point_self = 10
                                        # _*_^*|
                                        else:
                                            # *_*_^*|
                                            if i != 3 and j != self.chessboard_size - 4 and \
                                                    chessboard[i - 4][j + 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 1000
                                    # |*_^*|
                                    else:
                                        point_self = 0
                                # @_^*|
                                elif chessboard[i - 2][j + 2] == -self.color:
                                    point_self = 0
                                # __^*|
                                else:
                                    if i != 2 and j != self.chessboard_size - 3:
                                        #  *__^*|
                                        if chessboard[i - 3][j + 3] == self.color:
                                            # **__^*|
                                            if i != 3 and j != self.chessboard_size - 4 and \
                                                    chessboard[i - 4][j + 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 1000
                                        # @__^*|
                                        elif chessboard[i - 3][j + 3] == -self.color:
                                            point_self = 0
                                        # ___^*|
                                        else:
                                            # *___^*|
                                            if i != 3 and j != self.chessboard_size - 4 and \
                                                    chessboard[i - 4][j + 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 100
                                    # |__^*|
                                    else:
                                        point_self = 0
                            # |_^*|
                            else:
                                point_self = 0
                    # |^*|
                    else:
                        point_self = 0
            # ^@
            elif chessboard[i + 1][j - 1] == -self.color:
                if i != 0 and j != self.chessboard_size - 1:
                    # *^@
                    if chessboard[i - 1][j + 1] == self.color:
                        if i != 1 and j != self.chessboard_size - 2:
                            # **^@
                            if chessboard[i - 2][j + 2] == self.color:
                                if i != 2 and j != self.chessboard_size - 3:
                                    # ***^@
                                    if chessboard[i - 3][j + 3] == self.color:
                                        if i != 3 and j != self.chessboard_size - 4:
                                            # ****^@
                                            if chessboard[i - 4][j + 4] == self.color:
                                                point_self = 1000000
                                            # @***^@
                                            elif chessboard[i - 4][j + 4] == -self.color:
                                                point_self = 1
                                            # _***^@
                                            else:
                                                # *_***^@
                                                if i != 4 and j != self.chessboard_size - 5 and \
                                                        chessboard[i - 5][j + 5] == self.color:
                                                    point_self = 0
                                                else:
                                                    point_self = 10000
                                        # |***^@
                                        else:
                                            point_self = 0
                                    # @**^@
                                    elif chessboard[i - 3][j + 3] == -self.color:
                                        point_self = 0
                                    # _**^@
                                    else:
                                        point_self = 1000
                                # |**^@
                                else:
                                    point_self = 0
                            # @*^@
                            elif chessboard[i - 2][j + 2] == -self.color:
                                point_self = 0
                            # _*^@
                            else:
                                if i != 2 and j != self.chessboard_size - 3:
                                    # *_*^@
                                    if chessboard[i - 3][j + 3] == self.color:
                                        point_self = 100
                                    # @_*^@
                                    elif chessboard[i - 3][j + 3] == -self.color:
                                        point_self = 0
                                    # __*^@
                                    else:
                                        point_self = 1
                                # |_*^@
                                else:
                                    point_self = 0
                        # |*^@
                        else:
                            point_self = 0
                    # @^@
                    elif chessboard[i - 1][j + 1] == -self.color:
                        point_self = 0
                    # _^@
                    else:
                        if i != 1 and j != self.chessboard_size - 2:
                            # *_^@
                            if chessboard[i - 2][j + 2] == self.color:
                                point_self = 10
                            # @_^@
                            elif chessboard[i - 2][j + 2] == -self.color:
                                point_self = 0
                            # __^@
                            else:
                                point_self = 1
                        # |_^@
                        else:
                            point_self = 0
                # |^@
                else:
                    point_self = 0
            # ^_
            else:
                if i != self.chessboard_size - 2 and j != 1:
                    # ^_*
                    if chessboard[i + 2][j - 2] == self.color:
                        if i != 0 and j != self.chessboard_size - 1:
                            # *^_*
                            if chessboard[i - 1][j + 1] == self.color:
                                if i != 1 and j != self.chessboard_size - 2:
                                    # **^_*
                                    if chessboard[i - 2][j + 2] == self.color:
                                        if i != 2 and j != self.chessboard_size - 3:
                                            # ***^_*
                                            if chessboard[i - 3][j + 3] == self.color:
                                                if i != 3 and j != self.chessboard_size - 4:
                                                    # ****^_*
                                                    if chessboard[i - 4][j + 4] == self.color:
                                                        point_self = 1000000
                                                    # @***^_*
                                                    elif chessboard[i - 4][j + 4] == self.color:
                                                        point_self = 0
                                                    # _***^_*
                                                    else:
                                                        # *_***^_*
                                                        if i != 4 and j != self.chessboard_size - 5 and \
                                                                chessboard[i - 5][j + 5] == self.color:
                                                            point_self = 0
                                                        else:
                                                            point_self = 100000
                                                # |***^_*
                                                else:
                                                    point_self = 0
                                            # @**^_*
                                            elif chessboard[i - 3][j + 3] == -self.color:
                                                # @**^_**
                                                if i != self.chessboard_size - 3 and j != 2 and \
                                                        chessboard[i + 3][j - 3] == self.color:
                                                    point_self = 0
                                                else:
                                                    point_self = 10000
                                            # _**^_*
                                            else:
                                                point_self = 10000
                                        # |**^_*
                                        else:
                                            point_self = 10000
                                    # @*^_*
                                    elif chessboard[i - 2][j + 2] == -self.color:
                                        point_self = 10
                                    # _*^_*
                                    else:
                                        point_self = 10000
                                # |*^_*
                                else:
                                    point_self = 10
                            # @^_*
                            elif chessboard[i - 1][j + 1] == -self.color:
                                point_self = 1
                            # _^_*
                            else:
                                point_self = 1
                        # |^_*
                        else:
                            point_self = 0
                    # ^_@
                    elif chessboard[i + 2][j - 2] == -self.color:
                        if i != 0 and j != self.chessboard_size - 1:
                            # *^_@
                            if chessboard[i - 1][j + 1] == self.color:
                                if i != 1 and j != self.chessboard_size - 2:
                                    # **^_@
                                    if chessboard[i - 2][j + 2] == self.color:
                                        if i != 2 and j != self.chessboard_size - 3:
                                            # ***^_@
                                            if chessboard[i - 3][j + 3] == self.color:
                                                if i != 3 and j != self.chessboard_size - 4:
                                                    # ****^_@
                                                    if chessboard[i - 4][j + 4] == self.color:
                                                        point_self = 1000000
                                                    # @***^_@
                                                    elif chessboard[i - 4][j + 4] == -self.color:
                                                        point_self = 10000
                                                    # _***^_@
                                                    else:
                                                        point_self = 100000
                                                # |***^_@
                                                else:
                                                    point_self = 10000
                                            # @**^_@
                                            elif chessboard[i - 3][j + 3] == -self.color:
                                                point_self = 1
                                            # _**^_@
                                            else:
                                                point_self = 10000
                                        # |**^_@
                                        else:
                                            point_self = 1
                                    # @*^_@
                                    elif chessboard[i - 2][j + 2] == -self.color:
                                        point_self = 1
                                    # _*^_@
                                    else:
                                        point_self = 1
                                # |*^_@
                                else:
                                    point_self = 1
                            # @^_@
                            elif chessboard[i - 1][j + 1] == -self.color:
                                point_self = 1
                            # _^_@
                            else:
                                point_self = 1
                        # |^_@
                        else:
                            point_self = 1
                    # ^__
                    else:
                        if i != 0 and j != self.chessboard_size - 1:
                            # *^__
                            if chessboard[i - 1][j + 1] == self.color:
                                if i != 1 and j != self.chessboard_size - 2:
                                    # **^__
                                    if chessboard[i - 2][j + 2] == self.color:
                                        if i != 2 and j != self.chessboard_size - 3:
                                            # ***^__
                                            if chessboard[i - 3][j + 3] == self.color:
                                                if i != 3 and j != self.chessboard_size - 4:
                                                    # ****^__
                                                    if chessboard[i - 4][j + 4] == self.color:
                                                        point_self = 1000000
                                                    # @***^__
                                                    elif chessboard[i - 4][j + 4] == -self.color:
                                                        point_self = 10000
                                                    # _***^__
                                                    else:
                                                        point_self = 100000
                                                # |***^__
                                                else:
                                                    point_self = 10000
                                            # @**^__
                                            elif chessboard[i - 3][j + 3] == -self.color:
                                                point_self = 100
                                            # _**^__
                                            else:
                                                point_self = 10000
                                        # |**^__
                                        else:
                                            point_self = 100
                                    # @*^__
                                    elif chessboard[i - 2][j + 2] == -self.color:
                                        point_self = 50
                                    # _*^__
                                    else:
                                        if i != 2 and j != self.chessboard_size - 3:
                                            # *_*^__
                                            if chessboard[i - 3][j + 3] == self.color:
                                                point_self = 100
                                            # @_*^__
                                            elif chessboard[i - 3][j + 3] == -self.color:
                                                point_self = 100
                                            # __*^__
                                            else:
                                                point_self = 100
                                        # |_*^__
                                        else:
                                            point_self = 100
                                # |*^__
                                else:
                                    point_self = 1
                            # @^__
                            elif chessboard[i - 1][j + 1] == -self.color:
                                point_self = 1
                            # _^__
                            else:
                                point_self = 1
                        # |^__
                        else:
                            point_self = 0
                # ^_|
                else:
                    if i != 0 and j != self.chessboard_size - 1:
                        # *^_|
                        if chessboard[i - 1][j + 1] == self.color:
                            if i != 1 and j != self.chessboard_size - 2:
                                # **^_|
                                if chessboard[i - 2][j + 2] == self.color:
                                    if i != 2 and j != self.chessboard_size - 3:
                                        # ***^_|
                                        if chessboard[i - 3][j + 3] == self.color:
                                            if i != 3 and j != self.chessboard_size - 4:
                                                # ****^_|
                                                if chessboard[i - 4][j + 4] == self.color:
                                                    point_self = 1000000
                                                # @***^_|
                                                elif chessboard[i - 4][j + 4] == -self.color:
                                                    point_self = 10000
                                                # _***^_|
                                                else:
                                                    point_self = 100000
                                            # |***^_|
                                            else:
                                                point_self = 10000
                                        # @**^_|
                                        elif chessboard[i - 3][j + 3] == -self.color:
                                            point_self = 1
                                        # _**^_|
                                        else:
                                            point_self = 10000
                                    # |**^_|
                                    else:
                                        point_self = 0
                                # @*^_|
                                elif chessboard[i - 2][j + 2] == -self.color:
                                    point_self = 0
                                # _*^_|
                                else:
                                    # *_*^_|
                                    if i != 2 and j != self.chessboard_size - 3 and \
                                            chessboard[i - 3][j + 3] == self.color:
                                        point_self = 0
                                    else:
                                        point_self = 1000
                            # |*^_|
                            else:
                                point_self = 0
                        # @^_|
                        elif chessboard[i - 1][j + 1] == -self.color:
                            point_self = 0
                        # _^_|
                        else:
                            point_self = 0
                    # |^_|
                    else:
                        point_self = 0
        # ^|
        else:
            if i != 0 and j != self.chessboard_size - 1:
                # *^|
                if chessboard[i - 1][j + 1] == self.color:
                    if i != 1 and j != self.chessboard_size - 2:
                        # **^|
                        if chessboard[i - 2][j + 2] == self.color:
                            if i != 2 and j != self.chessboard_size - 3:
                                # ***^|
                                if chessboard[i - 3][j + 3] == self.color:
                                    if i != 3 and j != self.chessboard_size - 4:
                                        # ****^|
                                        if chessboard[i - 4][j + 4] == self.color:
                                            point_self = 1000000
                                        # @***^|
                                        elif chessboard[i - 4][j + 4] == -self.color:
                                            point_self = 1
                                        # _***^|
                                        else:
                                            # *_***^|
                                            if i != 4 and j != self.chessboard_size - 5 and \
                                                    chessboard[i - 5][j + 5] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 10000
                                    # |***^|
                                    else:
                                        point_self = 0
                                # @**^|
                                elif chessboard[i - 3][j + 3] == -self.color:
                                    point_self = 0
                                # _**^|
                                else:
                                    point_self = 0
                            # |**^|
                            else:
                                point_self = 0
                        # @*^|
                        elif chessboard[i - 2][j + 2] == -self.color:
                            point_self = 0
                        # _*^|
                        else:
                            point_self = 1
                    # |*^|
                    else:
                        point_self = 0
                # @^|
                elif chessboard[i - 1][j + 1] == -self.color:
                    point_self = 0
                # _^|
                else:
                    point_self = 1
            # |^|
            else:
                point_self = 0
        return point_self

    def checkNa(self, i, j, chessboard):
        if i != self.chessboard_size - 1 and j != self.chessboard_size - 1:
            # ^*
            if chessboard[i + 1][j + 1] == self.color:
                if i != self.chessboard_size - 2 and j != self.chessboard_size - 2:
                    # ^**
                    if chessboard[i + 2][j + 2] == self.color:
                        if i != self.chessboard_size - 3 and j != self.chessboard_size - 3:
                            # ^***
                            if chessboard[i + 3][j + 3] == self.color:
                                if i != self.chessboard_size - 4 and j != self.chessboard_size - 4:
                                    # ^****
                                    if chessboard[i + 4][j + 4] == self.color:
                                        point_self = 1000000
                                    # ^***@
                                    elif chessboard[i + 4][j + 4] == -self.color:
                                        if i != 0 and j != 0:
                                            # *^***@
                                            if chessboard[i - 1][j - 1] == self.color:
                                                point_self = 1000000
                                            # @^***@
                                            elif chessboard[i - 1][j - 1] == -self.color:
                                                point_self = 10
                                            # _^***@
                                            else:
                                                if i != 1 and j != 1:
                                                    # *_^***@
                                                    if chessboard[i - 2][j - 2] == self.color:
                                                        point_self = 0
                                                    # @_^***@ or __^***@ or |_^***@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                        # |^***@
                                        else:
                                            point_self = 10
                                    # ^***_
                                    else:
                                        if i != 0 and j != 0:
                                            # *^***_
                                            if chessboard[i - 1][j - 1] == self.color:
                                                if i != 1 and j != 1:
                                                    # **^***_
                                                    if chessboard[i - 2][j - 2] == self.color:
                                                        point_self = 0
                                                    # @*^***_ or _*^***_ or |*^***_
                                                    else:
                                                        point_self = 1000000
                                                else:
                                                    point_self = 1000000
                                            # @^***_
                                            elif chessboard[i - 1][j - 1] == -self.color:
                                                point_self = 10000
                                            # _^***_
                                            else:
                                                point_self = 100000
                                        # |^***_
                                        else:
                                            point_self = 10000
                                # ^***|
                                else:
                                    if i != 0 and j != 0:
                                        # *^***|
                                        if chessboard[i - 1][j - 1] == self.color:
                                            point_self = 1000000
                                        # @^***|
                                        elif chessboard[i - 1][j - 1] == -self.color:
                                            point_self = 0
                                        # _^***|
                                        else:
                                            point_self = 10000
                                    # |^***|
                                    else:
                                        point_self = 0
                            # ^**@
                            elif chessboard[i + 3][j + 3] == -self.color:
                                if i != 0 and j != 0:
                                    # *^**@
                                    if chessboard[i - 1][j - 1] == self.color:
                                        if i != 1 and j != 1:
                                            # **^**@
                                            if chessboard[i - 2][j - 2] == self.color:
                                                point_self = 1000000
                                            # @*^**@
                                            elif chessboard[i - 2][j - 2] == -self.color:
                                                point_self = 0
                                            # _*^**@
                                            else:
                                                point_self = 10000
                                        # |^**@
                                        else:
                                            point_self = 0
                                    # @^**@
                                    elif chessboard[i - 1][j - 1] == -self.color:
                                        point_self = 0
                                    # _^**@
                                    else:
                                        if i != 1 and j != 1:
                                            # *_^**@
                                            if chessboard[i - 2][j - 2] == self.color:
                                                if i != 2 and j != 2:
                                                    # **_^**@
                                                    if chessboard[i - 3][j - 3] == self.color:
                                                        point_self = 0
                                                    # @*_^**@ or _*_^**@ or |*_^**@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @_^**@
                                            elif chessboard[i - 2][j - 2] == -self.color:
                                                point_self = 0
                                            # __^**@
                                            else:
                                                if i != 2 and j != 2:
                                                    # *__^**@
                                                    if chessboard[i - 3][j - 3] == self.color:
                                                        point_self = 0
                                                    # @__^**@ or ___^**@ or |__^**@
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                        # |_^**@
                                        else:
                                            point_self = 0
                                # |^**@
                                else:
                                    point_self = 0
                            # ^**_
                            else:
                                if i != 0 and j != 0:
                                    # *^**_
                                    if chessboard[i - 1][j - 1] == self.color:
                                        if i != 1 and j != 1:
                                            # **^**_
                                            if chessboard[i - 2][j - 2] == self.color:
                                                if i != 2 and j != 2:
                                                    # ***^**_
                                                    if chessboard[i - 3][j - 3] == self.color:
                                                        point_self = 0
                                                    # @**^**_ or _**^**_ or |**^**_
                                                    else:
                                                        point_self = 1000000
                                                else:
                                                    point_self = 1000000
                                            # @*^**_
                                            elif chessboard[i - 2][j - 2] == -self.color:
                                                if i != self.chessboard_size - 4 and j != self.chessboard_size - 4:
                                                    # @*^**_*
                                                    if chessboard[i + 4][j + 4] == self.color:
                                                        point_self = 0
                                                    # @*^**_@ or @*^**__ or @*^**_|
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # _*^**_
                                            else:
                                                point_self = 100000
                                        # |*^**_
                                        else:
                                            point_self = 10000
                                    # @^**_
                                    elif chessboard[i - 1][j - 1] == -self.color:
                                        point_self = 100
                                    # _^**_
                                    else:
                                        if i != 1 and j != 1:
                                            # *_^**_
                                            if chessboard[i - 2][j - 2] == self.color:
                                                point_self = 10000
                                            # @_^**_
                                            elif chessboard[i - 2][j - 2] == -self.color:
                                                point_self = 10000
                                            # __^**_
                                            else:
                                                if i != 2 and j != 2:
                                                    # *__^**_
                                                    if chessboard[i - 3][j - 3] == self.color:
                                                        point_self = 10000
                                                    # @__^**_
                                                    elif chessboard[i - 3][j - 3] == -self.color:
                                                        point_self = 10000
                                                    # ___^**_
                                                    else:
                                                        point_self = 10000
                                                # |__^**_
                                                else:
                                                    point_self = 10000
                                        # |_^**_
                                        else:
                                            point_self = 100
                                # |^**_
                                else:
                                    point_self = 100
                        # ^**|
                        else:
                            if i != 0 and j != 0:
                                # *^**|
                                if chessboard[i - 1][j - 1] == self.color:
                                    if i != 1 and j != 1:
                                        # **^**|
                                        if chessboard[i - 2][j - 2] == self.color:
                                            point_self = 1000000
                                        # @*^**|
                                        elif chessboard[i - 2][j - 2] == -self.color:
                                            point_self = 0
                                        # _*^**|
                                        else:
                                            point_self = 10000
                                    # |*^**|
                                    else:
                                        point_self = 0
                                # @^**|
                                elif chessboard[i - 1][j - 1] == -self.color:
                                    point_self = 0
                                # _^**|
                                else:
                                    if i != 1 and j != 1:
                                        # *_^**|
                                        if chessboard[i - 2][j - 2] == self.color:
                                            point_self = 10000
                                        # @_^**|
                                        elif chessboard[i - 2][j - 2] == -self.color:
                                            point_self = 0
                                        # __^**|
                                        else:
                                            point_self = 100
                                    # |_^**|
                                    else:
                                        point_self = 0
                            # |^**|
                            else:
                                point_self = 0
                    # ^*@
                    elif chessboard[i + 2][j + 2] == -self.color:
                        if i != 0 and j != 0:
                            # *^*@
                            if chessboard[i - 1][j - 1] == self.color:
                                if i != 1 and j != 1:
                                    # **^*@
                                    if chessboard[i - 2][j - 2] == self.color:
                                        if i != 2 and j != 2:
                                            # ***^*@
                                            if chessboard[i - 3][j - 3] == self.color:
                                                point_self = 1000000
                                            # @**^*@
                                            elif chessboard[i - 3][j - 3] == -self.color:
                                                point_self = 0
                                            # _**^*@
                                            else:
                                                point_self = 10000
                                        # |**^*@
                                        else:
                                            point_self = 0
                                    # @*^*@
                                    elif chessboard[i - 2][j - 2] == -self.color:
                                        point_self = 0
                                    # _*^*@
                                    else:
                                        if i != 2 and j != 2:
                                            # *_*^*@
                                            if chessboard[i - 3][j - 3] == self.color:
                                                if i != 3 and j != 3:
                                                    # **_*^*@
                                                    if chessboard[i - 4][j - 4] == self.color:
                                                        point_self = 0
                                                    # @*_*^*@ or _*_*^*@ or |*_*^*@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @_*^*@
                                            elif chessboard[i - 3][j - 3] == -self.color:
                                                point_self = 0
                                            # __*^*@
                                            else:
                                                if i != 3 and j != 3:
                                                    # *__*^*@
                                                    if chessboard[i - 4][j - 4] == self.color:
                                                        point_self = 0
                                                    # @__*^*@ or ___*^*@ or |__*^*@
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                        # |_*^*@
                                        else:
                                            point_self = 0
                                # |*^*@
                                else:
                                    point_self = 0
                            # @^*@
                            elif chessboard[i - 1][j - 1] == -self.color:
                                point_self = 0
                            # _^*@
                            else:
                                if i != 1 and j != 1:
                                    # *_^*@
                                    if chessboard[i - 2][j - 2] == self.color:
                                        if i != 2 and j != 2:
                                            # **_^*@
                                            if chessboard[i - 3][j - 3] == self.color:
                                                if i != 3 and j != 3:
                                                    # ***_^*@
                                                    if chessboard[i - 4][j - 4] == self.color:
                                                        point_self = 0
                                                    # @**_^*@ or _**_^*@ or |**_^*@
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # @*_^*@
                                            elif chessboard[i - 3][j - 3] == -self.color:
                                                point_self = 0
                                            # _*_^*@
                                            else:
                                                if i != 3 and j != 3:
                                                    # *_*_^*@
                                                    if chessboard[i - 4][j - 4] == self.color:
                                                        point_self = 0
                                                    # @_*_^*@ or __*_^*@ or |_*_^*@
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                        # |*_^*@
                                        else:
                                            point_self = 0
                                    # @_^*@
                                    elif chessboard[i - 2][j - 2] == -self.color:
                                        point_self = 0
                                    # __^*@
                                    else:
                                        if i != 2 and j != 2:
                                            # *__^*@
                                            if chessboard[i - 3][j - 3] == self.color:
                                                if i != 3 and j != 3:
                                                    # **__^*@
                                                    if chessboard[i - 4][j - 4] == self.color:
                                                        point_self = 0
                                                    # @*__^*@ or _*__^* or |*__^*
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                            # @__^*@
                                            elif chessboard[i - 3][j - 3] == -self.color:
                                                point_self = 0
                                            # ___^*@
                                            else:
                                                if i != 3 and j != 3:
                                                    # *___^*@
                                                    if chessboard[i - 4][j - 4] == self.color:
                                                        point_self = 0
                                                    # @___^*@ or ____^*@ or |___^*@
                                                    else:
                                                        point_self = 10
                                                else:
                                                    point_self = 10
                                        # |__^*@
                                        else:
                                            point_self = 0
                                # |_^*@
                                else:
                                    point_self = 0
                        # |^*@
                        else:
                            point_self = 0
                    # ^*_
                    else:
                        if i != self.chessboard_size - 3 and j != self.chessboard_size - 3:
                            # ^*_*
                            if chessboard[i + 3][j + 3] == self.color:
                                if i != 0 and j != 0:
                                    # *^*_*
                                    if chessboard[i - 1][j - 1] == self.color:
                                        if i != 1 and j != 1:
                                            # **^*_*
                                            if chessboard[i - 2][j - 2] == self.color:
                                                if i != 2 and j != 2:
                                                    # ***^*_*
                                                    if chessboard[i - 3][j - 3] == self.color:
                                                        if i != 3 and j != 3:
                                                            # ****^*_*
                                                            if chessboard[i - 4][j - 4] == self.color:
                                                                point_self = 0
                                                            # @***^*_* or _***^*_* or |***^*_*
                                                            else:
                                                                point_self = 1000000
                                                        else:
                                                            point_self = 1000000
                                                    # @**^*_*
                                                    elif chessboard[i - 3][j - 3] == -self.color:
                                                        point_self = 0
                                                    # _**^*_*
                                                    else:
                                                        if i != 3 and j != 3:
                                                            # *_**^*_*
                                                            if chessboard[i - 4][j - 4] == self.color:
                                                                point_self = 0
                                                            # @_**^*_* or __**^*_* or |_**^*_*
                                                            else:
                                                                point_self = 100000
                                                        else:
                                                            point_self = 100000
                                                # |**^*_*
                                                else:
                                                    point_self = 0
                                            # @*^*_*
                                            elif chessboard[i - 2][j - 2] == -self.color:
                                                if i != self.chessboard_size - 4 and j != self.chessboard_size - 4:
                                                    # @*^*_**
                                                    if chessboard[i + 4][j + 4] == self.color:
                                                        point_self = 0
                                                    # @*^*_*@ or @*^*_*_ or @*^*_*|
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000
                                            # _*^*_*
                                            else:
                                                if i != 2 and j != 2:
                                                    # *_*^*_*
                                                    if chessboard[i - 3][j - 3] == self.color:
                                                        # **_*^*_**
                                                        if i != self.chessboard_size - 4 and \
                                                                j != self.chessboard_size - 4 \
                                                                and i != 3 and j != 3 \
                                                                and chessboard[i - 4][j - 4] == self.color \
                                                                and chessboard[i + 4][j + 4] == self.color:
                                                            point_self = 0
                                                        else:
                                                            point_self = 10000
                                                    # @_*^*_* or __*^*_*
                                                    else:
                                                        if i != self.chessboard_size - 4 and \
                                                                j != self.chessboard_size - 4:
                                                            # @_*^*_** or __*^*_**
                                                            if chessboard[i + 4][j + 4] == self.color:
                                                                point_self = 0
                                                            # @_*^*_*@ or @_*^*_*_ or @_*^*_*| or
                                                            # __*^*_*@ or __*^*_*_ or __*^*_*|
                                                            else:
                                                                point_self = 10000
                                                        else:
                                                            point_self = 10000
                                                # |_*^*_*
                                                else:
                                                    if i != self.chessboard_size - 4 and j != self.chessboard_size - 4:
                                                        # |_*^*_**
                                                        if chessboard[i + 4][j + 4] == self.color:
                                                            point_self = 0
                                                        # |_*^*_*@ or |_*^*_*_ or |_*^*_*|
                                                        else:
                                                            point_self = 10000
                                                    else:
                                                        point_self = 10000
                                        # |*^*_*
                                        else:
                                            if i != self.chessboard_size - 4 and j != self.chessboard_size - 4:
                                                # |*^*_**
                                                if chessboard[i + 4][j + 4] == self.color:
                                                    point_self = 0
                                                # |*^*_*@ or |*^*_*_ or |*^*_*|
                                                else:
                                                    point_self = 10000
                                            else:
                                                point_self = 10000
                                    # @^*_*
                                    elif chessboard[i - 1][j - 1] == -self.color:
                                        if i != self.chessboard_size - 4 and j != self.chessboard_size - 4:
                                            # @^*_**
                                            if chessboard[i + 4][j + 4] == self.color:
                                                # @^*_***
                                                if i != self.chessboard_size - 5 and \
                                                        j != self.chessboard_size - 5 and \
                                                        chessboard[i + 5][j + 5] == self.color:
                                                    point_self = 0
                                                else:
                                                    point_self = 10000
                                            # @^*_*@
                                            elif chessboard[i + 4][j + 4] == -self.color:
                                                point_self = 0
                                            # @^*_*_
                                            else:
                                                point_self = 100
                                        # @^*_*|
                                        else:
                                            point_self = 0
                                    # _^*_*
                                    else:
                                        if i != 1 and j != 1:
                                            # *_^*_*
                                            if chessboard[i - 2][j - 2] == self.color:
                                                point_self = 10000
                                            # @_^*_*
                                            elif chessboard[i - 2][j - 2] == -self.color:
                                                point_self = 100
                                            # __^*_*
                                            else:
                                                point_self = 100
                                        # |_^*_*
                                        else:
                                            point_self = 100
                                # |^*_*
                                else:
                                    point_self = 10
                            # ^*_@
                            elif chessboard[i + 3][j + 3] == -self.color:
                                if i != 0 and j != 0:
                                    # *^*_@
                                    if chessboard[i - 1][j - 1] == self.color:
                                        if i != 1 and j != 1:
                                            # **^*_@
                                            if chessboard[i - 2][j - 2] == self.color:
                                                if i != 2 and j != 2:
                                                    # ***^*_@
                                                    if chessboard[i - 3][j - 3] == self.color:
                                                        # ****^*_@
                                                        if i != 3 and j != 3 and \
                                                                chessboard[i - 4][j - 4] == self.color:
                                                            point_self = 0
                                                        else:
                                                            point_self = 1000000
                                                    # @**^*_@
                                                    elif chessboard[i - 3][j - 3] == -self.color:
                                                        point_self = 10000
                                                    # _**^*_@
                                                    else:
                                                        point_self = 100000
                                                # |**^*_@
                                                else:
                                                    point_self = 10000
                                            # @*^*_@
                                            elif chessboard[i - 2][j - 2] == -self.color:
                                                point_self = 0
                                            # _*^*_@
                                            else:
                                                point_self = 10000
                                        # |*^*_@
                                        else:
                                            point_self = 0
                                    # @^*_@
                                    elif chessboard[i - 1][j - 1] == -self.color:
                                        point_self = 1
                                    # _^*_@
                                    else:
                                        point_self = 1000
                                # |^*_@
                                else:
                                    point_self = 1
                            # ^*__
                            else:
                                if i != 0 and j != 0:
                                    # *^*__
                                    if chessboard[i - 1][j - 1] == self.color:
                                        if i != 1 and j != 1:
                                            # **^*__
                                            if chessboard[i - 2][j - 2] == self.color:
                                                if i != 2 and j != 2:
                                                    # ***^*__
                                                    if chessboard[i - 3][j - 3] == self.color:
                                                        if i != 3 and j != 3:
                                                            # ****^*__
                                                            if chessboard[i - 4][j - 4] == self.color:
                                                                point_self = 0
                                                            # @***^*_ or _***^*_ or |***^*_
                                                            else:
                                                                point_self = 1000000
                                                        else:
                                                            point_self = 1000000
                                                    # @**^*__
                                                    elif chessboard[i - 3][j - 3] == -self.color:
                                                        point_self = 10000
                                                    # _**^*__
                                                    else:
                                                        point_self = 100000
                                                # |**^*__
                                                else:
                                                    point_self = 10000
                                            # @*^*__
                                            elif chessboard[i - 3][j - 3] == -self.color:
                                                if i != self.chessboard_size - 4 and j != self.chessboard_size - 4:
                                                    # @*^*__*
                                                    if chessboard[i + 4][j + 4] == self.color:
                                                        point_self = 0
                                                    # @*^*__@ or @*^*___ or @*^*__|
                                                    else:
                                                        point_self = 1000
                                                else:
                                                    point_self = 1000
                                            # _*^*__
                                            else:
                                                if i != 2 and j != 2:
                                                    # *_*^*__
                                                    if chessboard[i - 3][j - 3] == self.color:
                                                        if i != 3 and j != 3:
                                                            # **_*^*__
                                                            if chessboard[i - 4][j - 4] == self.color:
                                                                if i != self.chessboard_size - 4 and \
                                                                        j != self.chessboard_size - 4:
                                                                    # **_*^*__*
                                                                    if chessboard[i + 4][j + 4] == self.color:
                                                                        point_self = 0
                                                                    # **_*^*__@ or **_*^*___ or **_*^*__|
                                                                    else:
                                                                        point_self = 1000
                                                                else:
                                                                    point_self = 1000
                                                            # @*_*^*__ or _*_*^*__ or |*_*^*__
                                                            else:
                                                                point_self = 10000
                                                        else:
                                                            point_self = 10000
                                                    # @_*^*__ or  __*^*__  or |_*^*__
                                                    else:
                                                        point_self = 10000
                                                else:
                                                    point_self = 10000

                                        # |*^*__
                                        else:
                                            if i != self.chessboard_size - 4 and j != self.chessboard_size - 4:
                                                # |*^*__*
                                                if chessboard[i + 4][j + 4] == self.color:
                                                    point_self = 0
                                                # |*^*__@ or |*^*___ or |*^*__|
                                                else:
                                                    point_self = 1000
                                            else:
                                                point_self = 1000
                                    # @^*__
                                    elif chessboard[i - 1][j - 1] == -self.color:
                                        point_self = 1
                                    # _^*__
                                    else:
                                        point_self = 1000
                                # |^*__
                                else:
                                    point_self = 1
                        # ^*_|
                        else:
                            if i != 0 and j != 0:
                                # *^*_|
                                if chessboard[i - 1][j - 1] == self.color:
                                    if i != 1 and j != 1:
                                        # **^*_|
                                        if chessboard[i - 2][j - 2] == self.color:
                                            point_self = 100000
                                        # @*^*_|
                                        elif chessboard[i - 2][j - 2] == -self.color:
                                            point_self = 0
                                        # _*^*_|
                                        else:
                                            if i != 2 and j != 2:
                                                # *_*^*_|
                                                if chessboard[i - 3][j - 3] == self.color:
                                                    # **_*^*|
                                                    if i != 3 and j != 3 and \
                                                            chessboard[i - 4][j - 4] == self.color:
                                                        point_self = 0
                                                    else:
                                                        point_self = 10000
                                                # @_*^*_| or __*^*_| or |_*^*_|
                                                else:
                                                    point_self = 10000
                                            else:
                                                point_self = 10000
                                    # |*^*_|
                                    else:
                                        point_self = 0
                                # @^*_|
                                elif chessboard[i - 1][j - 1] == -self.color:
                                    point_self = 0
                                # _^*_|
                                else:
                                    point_self = 100
                            # |^*_|
                            else:
                                point_self = 0
                # ^*|
                else:
                    if i != 0 and j != 0:
                        # *^*|
                        if chessboard[i - 1][j - 1] == self.color:
                            if i != 1 and j != 1:
                                # **^*|
                                if chessboard[i - 2][j - 2] == self.color:
                                    if i != 2 and j != 2:
                                        # ***^*|
                                        if chessboard[i - 3][j - 3] == self.color:
                                            # ****^*|
                                            if i != 3 and j != 3 and \
                                                    chessboard[i - 4][j - 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 1000000
                                        # @**^*|
                                        elif chessboard[i - 3][j - 3] == -self.color:
                                            point_self = 1
                                        # _**^*|
                                        else:
                                            # *_**^*|
                                            if i != 3 and j != 3 and \
                                                    chessboard[i - 4][j - 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 10000
                                    # |**^*|
                                    else:
                                        point_self = 0
                                # @*^*|
                                elif chessboard[i - 2][j - 2] == -self.color:
                                    point_self = 0
                                # _*^*|
                                else:
                                    if i != 2 and j != 2:
                                        # *_*^*|
                                        if chessboard[i - 3][j - 3] == self.color:
                                            point_self = 10000
                                        # @_*^*|
                                        elif chessboard[i - 3][j - 3] == -self.color:
                                            point_self = 0
                                        # __*^*|
                                        else:
                                            # *__*^*|
                                            if i != 3 and j != 3 and \
                                                    chessboard[i - 4][j - 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 1000
                                    # |_*^*|
                                    else:
                                        point_self = 0
                            # |*^*|
                            else:
                                point_self = 0
                        # @^*|
                        elif chessboard[i - 1][j - 1] == -self.color:
                            point_self = 0
                        # _^*|
                        else:
                            if i != 1 and j != 1:
                                # *_^*|
                                if chessboard[i - 2][j - 2] == self.color:
                                    if i != 2 and j != 2:
                                        # **_^*|
                                        if chessboard[i - 3][j - 3] == self.color:
                                            # ***_^*|
                                            if i != 3 and j != 3 and \
                                                    chessboard[i - 4][j - 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 10000
                                        # @*_^*|
                                        elif chessboard[i - 3][j - 3] == -self.color:
                                            point_self = 10
                                        # _*_^*|
                                        else:
                                            # *_*_^*|
                                            if i != 3 and j != 3 and \
                                                    chessboard[i - 4][j - 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 1000
                                    # |*_^*|
                                    else:
                                        point_self = 0
                                # @_^*|
                                elif chessboard[i - 2][j - 2] == -self.color:
                                    point_self = 0
                                # __^*|
                                else:
                                    if i != 2 and j != 2:
                                        #  *__^*|
                                        if chessboard[i - 3][j - 3] == self.color:
                                            # **__^*|
                                            if i != 3 and j != 3 and \
                                                    chessboard[i - 4][j - 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 1000
                                        # @__^*|
                                        elif chessboard[i - 3][j - 3] == -self.color:
                                            point_self = 0
                                        # ___^*|
                                        else:
                                            # *___^*|
                                            if i != 3 and j != 3 and \
                                                    chessboard[i - 4][j - 4] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 100
                                    # |__^*|
                                    else:
                                        point_self = 0
                            # |_^*|
                            else:
                                point_self = 0
                    # |^*|
                    else:
                        point_self = 0
            # ^@
            elif chessboard[i + 1][j + 1] == -self.color:
                if i != 0 and j != 0:
                    # *^@
                    if chessboard[i - 1][j - 1] == self.color:
                        if i != 1 and j != 1:
                            # **^@
                            if chessboard[i - 2][j - 2] == self.color:
                                if i != 2 and j != 2:
                                    # ***^@
                                    if chessboard[i - 3][j - 3] == self.color:
                                        if i != 3 and j != 3:
                                            # ****^@
                                            if chessboard[i - 4][j - 4] == self.color:
                                                point_self = 1000000
                                            # @***^@
                                            elif chessboard[i - 4][j - 4] == -self.color:
                                                point_self = 1
                                            # _***^@
                                            else:
                                                # *_***^@
                                                if i != 4 and j != 4 and \
                                                        chessboard[i - 5][j - 5] == self.color:
                                                    point_self = 0
                                                else:
                                                    point_self = 10000
                                        # |***^@
                                        else:
                                            point_self = 0
                                    # @**^@
                                    elif chessboard[i - 3][j - 3] == -self.color:
                                        point_self = 0
                                    # _**^@
                                    else:
                                        point_self = 1000
                                # |**^@
                                else:
                                    point_self = 0
                            # @*^@
                            elif chessboard[i - 2][j - 2] == -self.color:
                                point_self = 0
                            # _*^@
                            else:
                                if i != 2 and j != 2:
                                    # *_*^@
                                    if chessboard[i - 3][j - 3] == self.color:
                                        point_self = 100
                                    # @_*^@
                                    elif chessboard[i - 3][j - 3] == -self.color:
                                        point_self = 0
                                    # __*^@
                                    else:
                                        point_self = 1
                                # |_*^@
                                else:
                                    point_self = 0
                        # |*^@
                        else:
                            point_self = 0
                    # @^@
                    elif chessboard[i - 1][j - 1] == -self.color:
                        point_self = 0
                    # _^@
                    else:
                        if i != 1 and j != 1:
                            # *_^@
                            if chessboard[i - 2][j - 2] == self.color:
                                point_self = 10
                            # @_^@
                            elif chessboard[i - 2][j - 2] == -self.color:
                                point_self = 0
                            # __^@
                            else:
                                point_self = 1
                        # |_^@
                        else:
                            point_self = 0
                # |^@
                else:
                    point_self = 0
            # ^_
            else:
                if i != self.chessboard_size - 2 and j != self.chessboard_size - 2:
                    # ^_*
                    if chessboard[i + 2][j + 2] == self.color:
                        if i != 0 and j != 0:
                            # *^_*
                            if chessboard[i - 1][j - 1] == self.color:
                                if i != 1 and j != 1:
                                    # **^_*
                                    if chessboard[i - 2][j - 2] == self.color:
                                        if i != 2 and j != 2:
                                            # ***^_*
                                            if chessboard[i - 3][j - 3] == self.color:
                                                if i != 3 and j != 3:
                                                    # ****^_*
                                                    if chessboard[i - 4][j - 4] == self.color:
                                                        point_self = 1000000
                                                    # @***^_*
                                                    elif chessboard[i - 4][j - 4] == self.color:
                                                        point_self = 0
                                                    # _***^_*
                                                    else:
                                                        # *_***^_*
                                                        if i != 4 and j != 4 and \
                                                                chessboard[i - 5][j - 5] == self.color:
                                                            point_self = 0
                                                        else:
                                                            point_self = 100000
                                                # |***^_*
                                                else:
                                                    point_self = 0
                                            # @**^_*
                                            elif chessboard[i - 3][j - 3] == -self.color:
                                                # @**^_**
                                                if i != self.chessboard_size - 3 and j != self.chessboard_size - 3 and \
                                                        chessboard[i + 3][j + 3] == self.color:
                                                    point_self = 0
                                                else:
                                                    point_self = 10000
                                            # _**^_*
                                            else:
                                                point_self = 10000
                                        # |**^_*
                                        else:
                                            point_self = 10000
                                    # @*^_*
                                    elif chessboard[i - 2][j - 2] == -self.color:
                                        point_self = 10
                                    # _*^_*
                                    else:
                                        point_self = 10000
                                # |*^_*
                                else:
                                    point_self = 10
                            # @^_*
                            elif chessboard[i - 1][j - 1] == -self.color:
                                point_self = 1
                            # _^_*
                            else:
                                point_self = 1
                        # |^_*
                        else:
                            point_self = 0
                    # ^_@
                    elif chessboard[i + 2][j + 2] == -self.color:
                        if i != 0 and j != 0:
                            # *^_@
                            if chessboard[i - 1][j - 1] == self.color:
                                if i != 1 and j != 1:
                                    # **^_@
                                    if chessboard[i - 2][j - 2] == self.color:
                                        if i != 2 and j != 2:
                                            # ***^_@
                                            if chessboard[i - 3][j - 3] == self.color:
                                                if i != 3 and j != 3:
                                                    # ****^_@
                                                    if chessboard[i - 4][j - 4] == self.color:
                                                        point_self = 1000000
                                                    # @***^_@
                                                    elif chessboard[i - 4][j - 4] == -self.color:
                                                        point_self = 10000
                                                    # _***^_@
                                                    else:
                                                        point_self = 100000
                                                # |***^_@
                                                else:
                                                    point_self = 10000
                                            # @**^_@
                                            elif chessboard[i - 3][j - 3] == -self.color:
                                                point_self = 1
                                            # _**^_@
                                            else:
                                                point_self = 10000
                                        # |**^_@
                                        else:
                                            point_self = 1
                                    # @*^_@
                                    elif chessboard[i - 2][j - 2] == -self.color:
                                        point_self = 1
                                    # _*^_@
                                    else:
                                        point_self = 1
                                # |*^_@
                                else:
                                    point_self = 1
                            # @^_@
                            elif chessboard[i - 1][j - 1] == -self.color:
                                point_self = 1
                            # _^_@
                            else:
                                point_self = 1
                        # |^_@
                        else:
                            point_self = 1
                    # ^__
                    else:
                        if i != 0 and j != 0:
                            # *^__
                            if chessboard[i - 1][j - 1] == self.color:
                                if i != 1 and j != 1:
                                    # **^__
                                    if chessboard[i - 2][j - 2] == self.color:
                                        if i != 2 and j != 2:
                                            # ***^__
                                            if chessboard[i - 3][j - 3] == self.color:
                                                if i != 3 and j != 3:
                                                    # ****^__
                                                    if chessboard[i - 4][j - 4] == self.color:
                                                        point_self = 1000000
                                                    # @***^__
                                                    elif chessboard[i - 4][j - 4] == -self.color:
                                                        point_self = 10000
                                                    # _***^__
                                                    else:
                                                        point_self = 100000
                                                # |***^__
                                                else:
                                                    point_self = 10000
                                            # @**^__
                                            elif chessboard[i - 3][j - 3] == -self.color:
                                                point_self = 100
                                            # _**^__
                                            else:
                                                point_self = 10000
                                        # |**^__
                                        else:
                                            point_self = 100
                                    # @*^__
                                    elif chessboard[i - 2][j - 2] == -self.color:
                                        point_self = 50
                                    # _*^__
                                    else:
                                        if i != 2 and j != 2:
                                            # *_*^__
                                            if chessboard[i - 3][j - 3] == self.color:
                                                point_self = 100
                                            # @_*^__
                                            elif chessboard[i - 3][j - 3] == -self.color:
                                                point_self = 100
                                            # __*^__
                                            else:
                                                point_self = 100
                                        # |_*^__
                                        else:
                                            point_self = 100
                                # |*^__
                                else:
                                    point_self = 1
                            # @^__
                            elif chessboard[i - 1][j - 1] == -self.color:
                                point_self = 1
                            # _^__
                            else:
                                point_self = 1
                        # |^__
                        else:
                            point_self = 0
                # ^_|
                else:
                    if i != 0 and j != 0:
                        # *^_|
                        if chessboard[i - 1][j - 1] == self.color:
                            if i != 1 and j != 1:
                                # **^_|
                                if chessboard[i - 2][j - 2] == self.color:
                                    if i != 2 and j != 2:
                                        # ***^_|
                                        if chessboard[i - 3][j - 3] == self.color:
                                            if i != 3 and j != 3:
                                                # ****^_|
                                                if chessboard[i - 4][j - 4] == self.color:
                                                    point_self = 1000000
                                                # @***^_|
                                                elif chessboard[i - 4][j - 4] == -self.color:
                                                    point_self = 10000
                                                # _***^_|
                                                else:
                                                    point_self = 100000
                                            # |***^_|
                                            else:
                                                point_self = 10000
                                        # @**^_|
                                        elif chessboard[i - 3][j - 3] == -self.color:
                                            point_self = 1
                                        # _**^_|
                                        else:
                                            point_self = 10000
                                    # |**^_|
                                    else:
                                        point_self = 0
                                # @*^_|
                                elif chessboard[i - 2][j - 2] == -self.color:
                                    point_self = 0
                                # _*^_|
                                else:
                                    # *_*^_|
                                    if i != 2 and j != 2 and \
                                            chessboard[i - 3][j - 3] == self.color:
                                        point_self = 0
                                    else:
                                        point_self = 1000
                            # |*^_|
                            else:
                                point_self = 0
                        # @^_|
                        elif chessboard[i - 1][j - 1] == -self.color:
                            point_self = 0
                        # _^_|
                        else:
                            point_self = 0
                    # |^_|
                    else:
                        point_self = 0
        # ^|
        else:
            if i != 0 and j != 0:
                # *^|
                if chessboard[i - 1][j - 1] == self.color:
                    if i != 1 and j != 1:
                        # **^|
                        if chessboard[i - 2][j - 2] == self.color:
                            if i != 2 and j != 2:
                                # ***^|
                                if chessboard[i - 3][j - 3] == self.color:
                                    if i != 3 and j != 3:
                                        # ****^|
                                        if chessboard[i - 4][j - 4] == self.color:
                                            point_self = 1000000
                                        # @***^|
                                        elif chessboard[i - 4][j - 4] == -self.color:
                                            point_self = 1
                                        # _***^|
                                        else:
                                            # *_***^|
                                            if i != 4 and j != 4 and \
                                                    chessboard[i - 5][j - 5] == self.color:
                                                point_self = 0
                                            else:
                                                point_self = 10000
                                    # |***^|
                                    else:
                                        point_self = 0
                                # @**^|
                                elif chessboard[i - 3][j - 3] == -self.color:
                                    point_self = 0
                                # _**^|
                                else:
                                    point_self = 0
                            # |**^|
                            else:
                                point_self = 0
                        # @*^|
                        elif chessboard[i - 2][j - 2] == -self.color:
                            point_self = 0
                        # _*^|
                        else:
                            point_self = 1
                    # |*^|
                    else:
                        point_self = 0
                # @^|
                elif chessboard[i - 1][j - 1] == -self.color:
                    point_self = 0
                # _^|
                else:
                    point_self = 1
            # |^|
            else:
                point_self = 0
        return point_self

    # The input is current chessboard.
    def go(self, chessboard):
        # Clear candidate_list
        self.candidate_list.clear()
        # print("==================================================================")
        # Write your algorithm here

        da = -1
        new_pos = ()
        # print(self.color)
        for i in range(self.chessboard_size):
            print("   ")
            print(i)
            #print("   ")
            for j in range(self.chessboard_size):
                if chessboard[i][j] == 0:
                    x = self.checkLine(i, j, chessboard) + self.checkRow(i, j, chessboard) + \
                        self.checkPie(i, j, chessboard) + self.checkNa(i, j, chessboard)
                    self.color = -self.color
                    y = self.checkLine(i, j, chessboard) + self.checkRow(i, j, chessboard) + \
                        self.checkPie(i, j, chessboard) + self.checkNa(i, j, chessboard)
                    self.color = -self.color
                    t = x * 5 + y
                    print(x, y)
                    if t > da:
                        new_pos = (i, j)
                        da = t
            print(da)

        # print(new_pos)
        # print(da)
        # Here is the simplest sample:Random decision

        # idx = np.where(chessboard == COLOR_NONE)
        # idx = list(zip(idx[0], idx[1]))
        # pos_idx = random.randint(0, len(idx) - 1)
        # new_pos = idx[pos_idx]

        # ==============Find new pos========================================
        # Make sure that the position of your decision in chess board is empty.
        # If not, return error.

        assert chessboard[new_pos[0], new_pos[1]] == COLOR_NONE
        # Add your decision into candidate_list, Records the chess board

        self.candidate_list.append(new_pos)
