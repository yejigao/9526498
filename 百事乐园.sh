#!/bin/bash

#pepcoinbhhpre.pepcoinbypepsico.com.cn下的ck多账号@隔开 变量bslyck

accounts=$bslyck

if [[ -z "$accounts" ]]; then
    echo "你没有填入变量bslyck"
    exit
else
    IFS='@' read -ra accounts_list <<< "$accounts"
    num_of_accounts=${#accounts_list[@]}
    echo "共找到$num_of_accounts个账号,开始运行"
fi

function N {
    url="https://pepcoinbhhpre.pepcoinbypepsico.com.cn/mp/getDrawCount"

    #echo "==============抽奖=============="
    response=$(curl -s -H "token: $1" -H "content-type: application/json" -A "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/77777 MicroMessenger/8.0.45(0x18002d2a) NetType/4G Language/zh_CN" -X GET "$url")
    code=$(echo "$response" | jq -r '.code')

    if [[ $code -eq 0 ]]; then
        data=$(echo "$response" | jq -r '.data')
        echo "当前可以抽$data次"
        return 0
    else
        echo "登录失败"
        return 1
    fi
}

function Y {
    url="https://pepcoinbhhpre.pepcoinbypepsico.com.cn/mp/draw"

    response=$(curl -s -H "token: $1" -H "content-type: application/json" -A "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/77777 MicroMessenger/8.0.45(0x18002d2a) NetType/4G Language/zh_CN" -X GET "$url")
    code=$(echo "$response" | jq -r '.code')

    if [[ $code -eq 0 ]]; then
        name=$(echo "$response" | jq -r '.data.name')
        echo "抽奖-[$name]"
    else
        msg=$(echo "$response" | jq -r '.msg')
        echo "抽奖失败$msg"
    fi
}

index=1
for account in "${accounts_list[@]}"; do
    ck=$account
    echo "==============开始执行账号$index=============="
    if N "$ck"; then
        for ((i=0; i < data; i++)); do
            sleep 4
            Y "$ck"
        done
    fi
    ((index++))
done
