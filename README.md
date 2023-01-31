# face-recognition-with-faceNet
step 1 : clone github 
```
git clone https://github.com/anhalu/face-recognition-with-faceNet.git
```
step 2 : setup environment
```
conda create -n faces python=3.9
conda activate faces
conda install numpy 
conda install opencv-python
conda install pillow
conda install facenet-pytorch 
```
step 3 : get-data 
```
python get_data.py
#note : write name in console 
```
step 4 : create_facelist 
```
python create_facelst.py
```
step 5 : run face recognizer 
```
python face_recognition.py
```


![Screenshot from 2023-01-31 21-06-47](https://user-images.githubusercontent.com/89495585/215791409-d818c8d6-5e80-4856-9aec-cd482baa6d59.png)






>### I follow this Tutorial : https://viblo.asia/p/nhan-dien-khuon-mat-voi-mang-mtcnn-va-facenet-phan-2-bJzKmrVXZ9N


