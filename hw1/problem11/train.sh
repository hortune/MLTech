svm-train -s 0 -t 0 -c 0.00001  train_data model_0
svm-train -s 0 -t 0 -c 0.001  train_data model_1
svm-train -s 0 -t 0 -c 0.1  train_data model_2
svm-train -s 0 -t 0 -c 1  train_data model_3
svm-train -s 0 -t 0 -c 1000  train_data model_4

echo "=======-5======"
svm-predict test_data model_0 output0
echo "=======-3======"
svm-predict test_data model_1 output1
echo "=======-1======"
svm-predict test_data model_2 output2
echo "======= 1======"
svm-predict test_data model_3 output3
echo "======= 3======"
svm-predict test_data model_4 output4

