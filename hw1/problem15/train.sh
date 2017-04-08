svm-train -s 0 -t 2 -g 1 -c 0.1  train_data model_0
svm-train -s 0 -t 2 -g 10 -c 0.1  train_data model_1
svm-train -s 0 -t 2 -g 100 -c 0.1  train_data model_2
svm-train -s 0 -t 2 -g 1000 -c 0.1  train_data model_3
svm-train -s 0 -t 2 -g 10000 -c 0.1  train_data model_4

echo "=======-3======"
svm-predict test_data model_0 output0
echo "=======-2======"
svm-predict test_data model_1 output1
echo "=======-1======"
svm-predict test_data model_2 output2
echo "======= 0======"
svm-predict test_data model_3 output3
echo "======= 1======"
svm-predict test_data model_4 output4

