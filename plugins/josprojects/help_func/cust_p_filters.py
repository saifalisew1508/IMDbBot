#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pyrogram import (
    filters
)
from info import (
    ADMINS
)
from plugins.josprojects.help_func.admin_check import admin_check


def f_sudo_filter(filt, client, message):
    return message.from_user.id in ADMINS


sudo_filter = filters.create(
    func=f_sudo_filter,
    name="SudoFilter"
)


def onw_filter(filt, client, message):
    if ADMINS:
        return True
    else:
        return bool(
            message.from_user and
            message.from_user.is_self
        )


f_onw_fliter = filters.create(
    func=onw_filter,
    name="OnwFilter"
)


async def admin_filter_f(filt, client, message):
    return await admin_check(message)


admin_fliter = filters.create(
    func=admin_filter_f,
    name="AdminFilter"
)
