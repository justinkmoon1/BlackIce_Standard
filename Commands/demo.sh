#python tools/demo.py image -n yolox_tiny -c ./YOLOX_outputs/yolox_tiny/$1 --path ./assets/$2 --conf 0.25 --nms 0.45 --tsize 640 --save_result --device gpu
python tools/demo.py image -n yolox_tiny -c ./YOLOX_outputs/yolox_tiny/best_ckpt_ind.pth --path "C:/Users/Justin Moon/BlackIce/blackice_new.v4i.coco/test/IMG_1004-2_jpg.rf.87f08ca8ea1cba7eb927f9f0c71d26af.jpg" --conf 0.25 --nms 0.45 --tsize 640 --save_result --device gpu