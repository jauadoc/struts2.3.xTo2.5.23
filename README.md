# struts2.3.xTo2.5.23

## some script for update struts2.3.x to 2.5.23
> current find 3 situation will make project occur exception
>>1. in struts2.3.x tag: <s:* id=""/> is valid, but in 2.5.23 need change it to <s:* var=""/>, struts won't find ognl of this tag with id;
* contains [action,append,bean,date,generator,iterator,merge,number,set,sort,subset,text,url]
like <s:action> <s:append> and so on
