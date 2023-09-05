# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 14:20
# @Author  : Mandy


step = 15

id = 18 + step
phone = '151000000%d' % (16 + step)
time = '2023-03-31 15:55:%d' % (10 + step)
username = 'test%d' % (13 + step)
print(id,phone,time,username)

s1 = "insert into `gs_agent_user` (`create_time`, `deleted`, `id`, `password`, `phone`, `update_time`, `user_name`) " \
     "values ('%s', 0, '%d', '527180CD0106195DB1C10A3B04BAD778', '%s', '%s', '%s');" % (time, id, phone, time, username)

s2 = "insert into `gs_agent_user_third` (`app_id`, `app_type`, `create_time`, `deleted`, `id`, `last_login_time`, `nick_name`, `open_id`, `phone`, `type`, `union_id`, `update_time`, `user_id`) " \
     "values ('wx6c1740c7723d9210', 1, '%s', 0, '%d', '%s', NULL, 'oOrBT5dPmYSvqElU-74y86-ZwUBU', '%s', 1, '', '%s', '%d');" % (
     time, id, time, phone, time, id)

s3 = "insert into `gs_agent_user_third_admin_rel` (`admin_id`, `auth_time`, `create_time`, `id`, `update_time`, `user_third_id`) " \
     "values ('186293', '%s', '%s', '%d', '%s', '%d');" % (time, time, id, time, id)

print(s1)
print(s2)
print(s3)
