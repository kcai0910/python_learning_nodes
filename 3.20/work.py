"""
购物结算
用户输入结算金额与会员等级
1，购买商品去结算
2，如果大于500去走人工通道，否则自助结算
3，判断会员等级（普通会员打95折，高级会员打88折）
"""
if input('是否买东西:1:是 2：否\n')=='1':
    dollars = int(input('结算的金额:'))
    user1 = input('是否有会员：1：有   2：没有:\n')
    if user1 =='1':
        print('🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉')
        print('会员等级:1:%普通会员VIP%\t2:$高级会员SVIP$')
        print('🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉')
        member = input('请输入您的会员等级：')
    else:
        member = ''
    print(member)
    if dollars >500:
        print('这是人工通道')
        if member == '2':
            print(f'尊敬的高级会员，您一共消费了{dollars*0.88:.2f}$')
        elif member == '1':
            print(f'尊敬的会员，您一共消费了{dollars*0.95:.2f}$')
        else:
            print(f'尊敬的客人，您一共消费了{dollars}$')
        print('欢迎下次光临')
    else :
        print('这是自助结算')
        if member == '2':
            print(f'尊敬的高级会员，您一共消费了{dollars*0.88:.2f}$')
        elif member == '1':
            print(f'尊敬的会员，您一共消费了{dollars*0.95:.2f}$')
        else :
            print(f'尊敬的客人，您一共消费了{dollars}$')
        print('欢迎下次光临')
else :print('请慢走')