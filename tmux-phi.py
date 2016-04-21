#!/usr/bin/env python

import tmuxp


def phi(n):
    a = int(round(n / 1.618))
    b = n - a
    return (a, b)


server = tmuxp.Server()
session = server.list_sessions()[0]
window = session.attached_window()

window_height = int(window.get('window_height'))
window_width = int(window.get('window_width'))

main_width, secondary_width = phi(window_width)

current_pane = window.attached_pane()
current_pane.set_width(main_width)
current_pane.set_height(window_height)
