#!/bin/sh

ps -edf | grep -E '[p]ython.*flask' | awk '{ print $2}'  |xargs -n 1 kill -9
