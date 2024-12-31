# hass-heise
Home Assistant Heise online integration

 ```
<h1><img src="https://heise.cloudimg.io/v7/_www-heise-de_/download/media/heise-online-app-fuer-android-78501/heise-online-news-logo_1-1-30.png"  height="26"> Heise Online</h1>
{%- for i in range(2) %}
{%- set title = states("sensor.heiseonline_news_"~ loop.index) %}
{%- set updated = state_attr("sensor.heiseonline_news_"~ loop.index, "updated") %}
{%- set link = state_attr("sensor.heiseonline_news_"~ loop.index, "link") %}
{%- set summary = state_attr("sensor.heiseonline_news_"~ loop.index, "summary") %}
<a href="{{link}}"><b>{{title}}</b></a><br>
{{updated|as_datetime|time_since}} ago
<br/>
{%- if not loop.last %}<br>{%- endif %}
{%- endfor %}
 ```
