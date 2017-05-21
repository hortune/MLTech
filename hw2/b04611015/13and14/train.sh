svm-train -s 3 -t 2 -p 0.5 -c 0.001 -g 32  train model_0
svm-train -s 3 -t 2 -p 0.5 -c 0.001 -g 2 train model_1
svm-train -s 3 -t 2 -p 0.5 -c 0.001 -g 0.125  train model_2

svm-train -s 3 -t 2 -p 0.5 -c 1 -g 32  train model_3
svm-train -s 3 -t 2 -p 0.5 -c 1 -g 2 train model_4
svm-train -s 3 -t 2 -p 0.5 -c 1 -g 0.125  train model_5


svm-train -s 3 -t 2 -p 0.5 -c 1000 -g 32  train model_6
svm-train -s 3 -t 2 -p 0.5 -c 1000 -g 2 train model_7
svm-train -s 3 -t 2 -p 0.5 -c 1000 -g 0.125  train model_8
echo "=======0.001 32======"
svm-predict test_data model_0 output0
echo "=======0.001 2======"
svm-predict test_data model_1 output1
echo "=======0.001 0.125======"
svm-predict test_data model_2 output2
echo "=======1 32======"
svm-predict test_data model_3 output3
echo "=======1 2======"
svm-predict test_data model_4 output4
echo "=======1 0.125======"
svm-predict test_data model_5 output5
echo "=======1000 32======"
svm-predict test_data model_6 output6
echo "=======1000 2======"
svm-predict test_data model_7 output7
echo "=======1000 0.125======"
svm-predict test_data model_8 output8

echo "=======0.001 32======"
svm-predict train model_0 out0
echo "=======0.001 2======"
svm-predict train model_1 out1
echo "=======0.001 0.125======"
svm-predict train model_2 out2
echo "=======1 32======"
svm-predict train model_3 out3
echo "=======1 2======"
svm-predict train model_4 out4
echo "=======1 0.125======"
svm-predict train model_5 out5
echo "=======1000 32======"
svm-predict train model_6 out6
echo "=======1000 2======"
svm-predict train model_7 out7
echo "=======1000 0.125======"
svm-predict train model_8 out8
