#!/bin/sh

u="y"
while [ $u = "y" ]
do
   python ab1.py +6285236468370 &
   python ab1.py +6289524264559 &
   python ab1.py +6289676728844 &
   python ab1.py +6282232761985 &
   python ab1.py +13026046790 &
   python ab1.py +6281327312092

done
