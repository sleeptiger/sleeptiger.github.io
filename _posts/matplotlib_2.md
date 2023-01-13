# matplotlib.plyplot 모듈의 xlabel(), ylabel() 함수를 사용하여 레이블 표시


```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
plt.plot([1,2,3,4], [1,4,49,16])
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.show()

# plt.(xlabel/ylabel)('제목 이름 기재)
```


![png](matplotlib_2_files/matplotlib_2_2_0.png)



```python
plt.plot([1,2,3,4], [1,4,49,16])
plt.xlabel('X-Label', labelpad=15)
plt.ylabel('Y-Label', labelpad=20)
plt.show()

# labelpad = int -- 축과 떨어질 길이
```


![png](matplotlib_2_files/matplotlib_2_3_0.png)



```python
# font 설정  css 와 유사

font1 = {'family' : 'serif',
         'color' : 'b',
         'weight' : 'bold',
         'size' : 14
         }

font2 = {'family' : 'fantasy',
         'color' : 'deeppink',
         'weight' : 'normal',
         'size' : 'xx-large'
         }

plt.plot([1,2,3,4], [1,4,49,16])
plt.xlabel('X-Label', labelpad=15, fontdict = font1)
plt.ylabel('Y-Label', labelpad=20, fontdict = font2)
plt.show()

```


![png](matplotlib_2_files/matplotlib_2_4_0.png)


# Matplotlib.pylot 범례표시


```python
plt.plot([1,2,3,4], [1,3,5,10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()

plt.show()
```


![png](matplotlib_2_files/matplotlib_2_6_0.png)


- plot()함수에 label문자열을 지정하고 plt.legend()를 호출하면 위와 같이 범례가 출력된다.

#### 범례위치 지정 하기


```python
plt.plot([1,2,3,4], [1,3,5,10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(loc='lower right') # (lower/upper) + (left / right)

plt.show()
```


![png](matplotlib_2_files/matplotlib_2_9_0.png)


- 범례의 열 개수 지정하기


```python
plt.plot([1,2,3,4], [2,3,5,10], label='Price($)')
plt.plot([1,2,3,4], [3,5,9,7], label='Demand (#)')
plt.xlabel('X_Axis')
plt.ylabel('Y_Axis')

plt.legend(loc='best', ncol=1)
plt.show()
```


![png](matplotlib_2_files/matplotlib_2_11_0.png)



```python
plt.plot([1,2,3,4], [2,3,5,10], label='Price($)')
plt.plot([1,2,3,4], [3,5,9,7], label='Demand (#)')
plt.xlabel('X_Axis')
plt.ylabel('Y_Axis')

plt.legend(loc='best', ncol=2)
plt.show()
```


![png](matplotlib_2_files/matplotlib_2_12_0.png)


- fontsize 지정해주기



```python
plt.plot([1,2,3,4], [1,3,5,10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(loc='lower right', fontsize = 14)
plt.show()
```


![png](matplotlib_2_files/matplotlib_2_14_0.png)



```python
!jupyter nbconvert --to markdown '/content/drive/MyDrive/시각화'
```

    [NbConvertApp] Converting notebook /content/drive/MyDrive/시각화 to markdown
    Traceback (most recent call last):
      File "/usr/local/bin/jupyter-nbconvert", line 8, in <module>
        sys.exit(main())
      File "/usr/local/lib/python3.8/dist-packages/jupyter_core/application.py", line 277, in launch_instance
        return super().launch_instance(argv=argv, **kwargs)
      File "/usr/local/lib/python3.8/dist-packages/traitlets/config/application.py", line 992, in launch_instance
        app.start()
      File "/usr/local/lib/python3.8/dist-packages/nbconvert/nbconvertapp.py", line 340, in start
        self.convert_notebooks()
      File "/usr/local/lib/python3.8/dist-packages/nbconvert/nbconvertapp.py", line 510, in convert_notebooks
        self.convert_single_notebook(notebook_filename)
      File "/usr/local/lib/python3.8/dist-packages/nbconvert/nbconvertapp.py", line 481, in convert_single_notebook
        output, resources = self.export_single_notebook(notebook_filename, resources, input_buffer=input_buffer)
      File "/usr/local/lib/python3.8/dist-packages/nbconvert/nbconvertapp.py", line 410, in export_single_notebook
        output, resources = self.exporter.from_filename(notebook_filename, resources=resources)
      File "/usr/local/lib/python3.8/dist-packages/nbconvert/exporters/exporter.py", line 178, in from_filename
        with io.open(filename, encoding='utf-8') as f:
    IsADirectoryError: [Errno 21] Is a directory: '/content/drive/MyDrive/시각화'



```python

```
