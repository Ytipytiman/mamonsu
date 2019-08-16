#!/bin/bash
rval=`cat /proc/diskstats`

count=1
value=0
while read line; do
       if [[ ${line} != '' ]]; then
            IFS="|" values=(${line})

            if [[ $count == 1 ]]; then    # for loop0 case          
                new_value2=`echo ${values[0]} | sed -n '/[0-9]/s/ \+/ /gp'`
                new_value3=`echo "$new_value2" | cut -d " " -f 3`                
                write_op=`echo "$new_value2" | cut -d " " -f 8`
                
            else
                new_value2=`echo ${values[0]} | sed -n '/[0-9]/s/ \+/ /gp'`
                new_value3=`echo "$new_value2" | cut -d " " -f 4`
                
                write_op=`echo "$new_value2" | cut -d " " -f 9`
                
            fi
            re='^[0-9]+$'
            has_digits='no'    
            if [[ "${new_value3: -1}" =~ $re ]]; then
                  has_digits='yes'
            fi
            if [[ $new_value3 != *"loop"* ]]  &&  [[ $new_value3 != *"ram"* ]] &&  [[ $has_digits == 'no' ]];then
                #echo $write_op 

                value=$(($write_op+$value)) 
                 

            fi
          fi
    let "count=count+1"
done <<< ${rval}
echo $(($value))