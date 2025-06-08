import gradio as gr

def add(num1, num2):
    return num1 + num2

interface = gr.Interface(
    fn=add, 
    inputs = ['number', 'number'],
    outputs= 'number',
    title='계산기',
    description='숫자 두개를 입력하세요',
    #flag를 하지 않음 / flag를 누르면 .gradio파일이 생성되고 안에 값이 저장됨
    flagging_mode="never" 

)

interface.launch()