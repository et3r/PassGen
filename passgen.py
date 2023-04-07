#!/usr/bin/env python3

import menu

if __name__ == '__main__':

    all_menus = 0

    while(True):

        if all_menus == 0:
            menu.kw()
            option = menu.options()
        if all_menus == 1:
            option = menu.options()

        match option:
            case 1:
                print("gen")
                break # breaks the bucle, not the match statement
            case 2:
                menu.showkw()
                all_menus = 1
            case 3:
                all_menus = 0
                pass # pass, so the bucle starts again and menu() is executed again
            case 4:
                menu.editkw()
                all_menus = 1
            case _:
                print("\n[x] Choose a valid option!")
                all_menus = 1
