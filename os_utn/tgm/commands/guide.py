"""
This file contains classes with commands that guide
the user through the bot functionalities.
"""

import telegram
import telegram.ext
from os_utn.tgm.commands import text
from os_utn.tgm import context_buffer as cb
from os_utn.tgm.commands import example


class Guide:
    def start(update: telegram.Update, context: telegram.ext.CallbackContext):
        processes_scheduling_button = telegram.InlineKeyboardButton(
            text=text.PROCESSES_SCHEDULING_GUIDE_BUTTON,
            callback_data=cb.MainBuffer.PROCESSES_SCHEDULING_CALLBACK,
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.START_GUIDE,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup([[processes_scheduling_button]]),
        )

    def invalid_input(update: telegram.Update, context: telegram.ext.CallbackContext):
        processes_scheduling_button = telegram.InlineKeyboardButton(
            text=text.PROCESSES_SCHEDULING_GUIDE_BUTTON,
            callback_data=cb.MainBuffer.PROCESSES_SCHEDULING_CALLBACK,
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.START_GUIDE,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup([[processes_scheduling_button]]),
        )


class ProcessesScheduling:
    def select_processes_scheduling_algorithm(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        round_robin_button = telegram.InlineKeyboardButton(
            text=text.ROUND_ROBBIN_BUTTON,
            callback_data=cb.ProcessesSchedulingBuffer.RR_SA,
        )
        sjf_button = telegram.InlineKeyboardButton(
            text=text.SJF_BUTTON,
            callback_data=cb.ProcessesSchedulingBuffer.SJF_SA,
        )

        srtn_button = telegram.InlineKeyboardButton(
            text=text.SRTN_BUTTON,
            callback_data=cb.ProcessesSchedulingBuffer.SRTN_SA,
        )

        fcfs_button = telegram.InlineKeyboardButton(
            text=text.FCFS_BUTTON,
            callback_data=cb.ProcessesSchedulingBuffer.FCFS_SA,
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.SELECT_PROCESSES_SCHEDULING_ALGORITHM,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup(
                [[round_robin_button, sjf_button], [srtn_button, fcfs_button]]
            ),
        )

    def load_processes(update: telegram.Update, context: telegram.ext.CallbackContext):
        example_button = example.ExampleButton(
            cb.ProcessesSchedulingBuffer.PROCESSES_EI
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.LOAD_PROCESSES,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup([[example_button]]),
        )

    def round_robin_time_slice_and_modification(
        update: telegram.Update, context: telegram.ext.CallbackContext
    ):
        example_button = example.ExampleButton(
            cb.ProcessesSchedulingBuffer.RR_TIME_SLICE_AND_MODIFICATION_EI
        )

        chat_id = update.effective_user["id"]

        context.bot.sendMessage(
            parse_mode="MarkdownV2",
            text=text.RR_TIME_SLICE_AND_MODIFICATION,
            chat_id=chat_id,
            reply_markup=telegram.InlineKeyboardMarkup([[example_button]]),
        )
