# struts2.3.xTo2.5.23

## some script for update struts2.3.x to 2.5.23
> current find 3 situation will make project occur exception
>> 1. id to var;  
in struts2.3.x tag: <s:* id=""/> is valid, but in 2.5.23 need change it to <s:* var=""/>, struts won't find ognl of this tag with id;  
<s:*> contains [action,append,bean,date,generator,iterator,merge,number,set,sort,subset,text,url]
like <s:action> <s:append> and so on)
>> 2. <some tag/><s:text name="中文字符串"/><some tag/> to <som tag/>中文字符串<some tag/>  
in struts2.3.x tag <s:text name="中文字符串"/> is valid, but not in 2.5.23;()
>> 3. find field like aAaaa in java  
some field in java, like private String sText; struts can't find this field get/set function;  
you need write by hump like scriptText, not sText, sText auto create set/get setSText/getSText, make struts can't find get/set function
