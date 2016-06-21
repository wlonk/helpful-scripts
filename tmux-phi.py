#!/usr/bin/env python

from libtmux import server


def phi(n):
    a = int(round(n / 1.618))
    b = n - a
    return (a, b)


server = server.Server()
session = server.list_sessions()[0]
window = session.attached_window

window_width = int(window.get('window_width'))

main_width, _ = phi(window_width)

panes = window.panes
main_pane = window.panes[0]

window.split_window()
window.select_layout('main-vertical')

window_height = int(window.get('window_height'))
main_pane.set_width(main_width)
window.select_pane('1')
