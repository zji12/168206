# -*- coding:utf-8 -*-
'''
ʹ������Ԫ��˼�룬��ʱ�����ϸ��
��ʱ��ÿ10s��Ϊһ����Ԫ���з���
�����Ϊ�����֣�
A��      dis_table2      �����̨
B��      dis_fire        �����տ���
'''

#�Ͳ�����
number = 2
#����֮���ʱ����
interval = 0

#20����̨����ʹ��ʱ״̬λΪ 0
tables = dict.fromkeys(range(20), 0)
#�տ��ܿ�ͬʱ�տ�8���ˣ�ʹ��ʱ״̬λΪ 0
fires = dict.fromkeys(range(8), 0)
#ѡȡʳ�ĵ��ˣ�״̬λΪ�Ѿ�ѡȡ��ʳ�ĸ���
peoples = dict.fromkeys(range(number), 0)
#���ڽ���ѡȡʳ�ĵ�����
p_table_img = 0
#�Ѿ�ѡȡ��5��ʳ�ģ����Խ����տ�������
p_ready_to_fire = 0
#���ڽ����տ�������
p_fire_ing = 0
#��̨��ȡ5��ʳ�Ľ���������
p_table_done = 0
#�տ�����������
p_fire_done = 0
#��̨ʹ�ý����ı�־λ
flag_end_table = 0
#��̨ʹ�õ�ʱ��
time_total_table = 0
#���տ��ܵȴ���ʱ��
time_wait_fire = 0
#���оͲ��˻��ѵ�ʱ���ܺ�
time_total = 0
def dis_table2():
    '''
    ������Ҫѡȡʳ�ĵ���(peoples)����������̨ѡȡ5��ʳ��
    '''
    global p_table_img, p_ready_to_fire, peoples, flag_end_table, p_table_done, time_total
    if peoples.__len__():
        peoples_tmp = peoples.copy()
        for people_id, people_status in peoples_tmp.iteritems():
            time_total += 1
            if people_status == 0 and p_table_img < 20:
                p_table_img += 1
                peoples[people_id] += 1
            if people_status:
                peoples[people_id] += 1
                if people_status == 5:
                    p_ready_to_fire +=1
                    p_table_img -= 1
                    peoples.pop(people_id)
                    p_table_done += 1
    else:
        if p_table_done == number:
            flag_end_table = 1

def dis_fire():
    '''
    ��1���տ��ܿ���8������ʹ�õ��տ���(fires )
    ѡȡ��ʳ�ĵ���(p_ready_to_fire)������������ʹ�õ��տ���(fire_status ==0)
    '''
    global p_fire_ing, p_fire_done, p_ready_to_fire, fires, time_wait_fire, time_total
    if p_ready_to_fire > 8 - p_fire_ing:
        time_wait_fire += p_ready_to_fire - (8 - p_fire_ing)
    time_total += (p_ready_to_fire + p_fire_ing)
    for fire_id, fire_status in fires.iteritems():
        if fire_status == 0:
            if p_ready_to_fire > 0 :
                p_fire_ing += 1
                p_ready_to_fire -= 1
                fires[fire_id] += 1
        if fire_status:
            fires[fire_id] +=1
            if fires[fire_id] == 3* 6:
                fires[fire_id] = 0
                p_fire_done += 1
                p_fire_ing -= 1
                
def test(i,p_interval = 0):
    global peoples, p_need_to_table
    if p_interval:
        print p_interval,'p_interval'
        peoples = {}
    else:
        peoples = dict.fromkeys(range(number), 0)
    for n in range(i):
        if p_interval:
            if not n % p_interval :
                p_have = n // p_interval
                if p_have < number:
                    peoples[p_have] = 0
        if flag_end_table:
            print n
        dis_table2()
        dis_fire()

def result(p_interval = 0):
    global peoples, p_need_to_table, flag_end_table, time_total_table
    if p_interval:
        peoples = {}
    else:
        peoples = dict.fromkeys(range(number), 0)
    n = 0
    while p_fire_done < number:
        if p_interval:
            if not n % p_interval :
                p_have = n // p_interval
                if p_have < number:
                    peoples[p_have] = 0
        if not flag_end_table:
            dis_table2()
            time_total_table = n
        dis_fire()
        n += 1
    return n

def output_form(people_count, interval_b_p):
    #�����˵ȴ�+ȡʳ��+���տ���ʱ��Ϊtime_total - people_count
    time_av = (time_total - people_count)  * 10.0 / people_count 
    #���������տ��ܵȴ���ʱ��Ϊtime_wait_fire
    time_av_fire = time_wait_fire * 10.0 / people_count 
    #��̨�ӿ�ʼ������ʹ�õ�ʱ��Ϊtime_total_table - 1
    #���а�������֮��ļ��ʱ��(people_count - 1) * interval_b_p
    #ԭ���ϣ����Ŷӵȴ����ڰ�̨�ķѵ�ƽ��ʱ��Ϊ5
    time_av_table = ((time_total_table - 1 ) - (people_count - 1) * interval_b_p - 5)
    time_av_table = time_av_table * 10.0 / people_count 
    interval_b_p = interval_b_p / 6.0
    print "��%s���˿ͣ��������ʱ��Ϊ%s����ʱ,ƽ��ÿλ�˿͵Ĳ�ʳ׼��ʱ��Ϊ%s��" %(people_count, interval_b_p, time_av)
    print "�˿����տ��ܵ�ƽ���ȴ�ʱ��Ϊ%s��" % time_av_fire
    print "�˿��ڰ�̨��ƽ���ȴ�ʱ��Ϊ%s��" % time_av_table
    

number = 2
interval = 0
#test(226,12)
n = result(interval)
print  time_total
output_form(number, interval)