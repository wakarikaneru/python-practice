import io
import sys
import re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Hello Prime world!")

args = sys.argv

expr = args[1]
print("落ち着いて" + str(expr) + " を計算するんだ…")

# 逆ポーランド法に変換
# 下準備…
add = "+"
sub = "-"
mul = "*"
div = "/"
lp = "("
rp = ")"
eq = "="

# 優先度の設定
priority = {"num": 0, "+": 1, "-": 1, "*": 2,
            "/": 2, "(": 3, ")": 3, "=": 0}

# トークンから優先度を返す関数を作っておく


def getPriority(token):
    tokenType = token
    if tokenType is None:
        return 0
    if re.match(r"\d+", tokenType):
        tokenType = "num"
    # 優先度を取得
    p = priority[tokenType]
    # print("priority: " + str(p))
    return p

# トークンに分割
tokenizeExpr = expr.split(" ")

# トークンをバッファに詰め込んでいく
# 参考:http://home.a00.itscom.net/hatada/c-tips/rpn/rpn02.html
# ()の動きは未実装。このあたりに処理を追加すれば行けそう…
tempOpe = []
buff = []
tempPriority = 0

for i in tokenizeExpr:
    # print(i)
    # 優先度を取得
    nowPriority = getPriority(i)

    # 詰め込む
    if nowPriority == priority["num"]:
        buff.append(i)
    else:
        while 0 < len(tempOpe):
            tempPriority = getPriority(tempOpe[len(tempOpe) - 1])
            if nowPriority <= tempPriority:
                buff.append(tempOpe.pop())
            elif tempPriority < nowPriority:
                break
        tempOpe.append(i)

while 0 < len(tempOpe):
    buff.append(tempOpe.pop())

# バッファを表示
print(buff)

# 逆ポーランド法に変換された式を計算する
# 計算用スタックを準備する
stack = []
for i in buff:
    if re.match(r"\d+", i):
        stack.append(int(i))
    else:
        if i==add:
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2+n1)
        if i==sub:
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
        if i==mul:
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)
        if i==div:
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)

    # 計算結果を表示
print(str(expr) + " = " + str(stack[0]))
