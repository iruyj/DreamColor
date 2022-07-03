import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def mark(value):
    # nl2br(줄바꿈), fenced_code(마크다운을 소스코드로 변환)
    # nl2br을 사용하지 않을 경우 줄바꿈을 하기 위해서는 줄 끝에 스페이스(' ')를 두개 연속으로 입력해야 한다.
    extensions = ["nl2br","fenced_code"]
    return mark_safe(markdown.markdown(value,extensions=extensions))