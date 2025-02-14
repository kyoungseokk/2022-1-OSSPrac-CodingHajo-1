from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')  # default URL
def student():
   return render_template('input_info.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Namezz'] = request.form.get('Namezz')
      result['Univ'] = request.form.get('Univ')
      result['Student Number'] = request.form.get('Student Number')
      result['Gender'] = request.form.get('Gender')
      result['Major'] = request.form.get('Major')
      result['languages'] = request.form.getlist('languages')
      result['languages'] =  ','.join(result['languages'])

      # 학번
      # 대학
      # 성별
      # 학과
      # 프로그래밍 언어 -> hint) ','.join(list명)을 사용하면 list 안에 있는 항목들이 ','로 나누어져 출력됨.

      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run()
