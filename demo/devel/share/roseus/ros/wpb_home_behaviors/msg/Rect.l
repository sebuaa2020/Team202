;; Auto-generated. Do not edit!


(when (boundp 'wpb_home_behaviors::Rect)
  (if (not (find-package "WPB_HOME_BEHAVIORS"))
    (make-package "WPB_HOME_BEHAVIORS"))
  (shadow 'Rect (find-package "WPB_HOME_BEHAVIORS")))
(unless (find-package "WPB_HOME_BEHAVIORS::RECT")
  (make-package "WPB_HOME_BEHAVIORS::RECT"))

(in-package "ROS")
;;//! \htmlinclude Rect.msg.html


(defclass wpb_home_behaviors::Rect
  :super ros::object
  :slots (_name _top _bottom _left _right _probability ))

(defmethod wpb_home_behaviors::Rect
  (:init
   (&key
    ((:name __name) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:top __top) (make-array 0 :initial-element 0 :element-type :integer))
    ((:bottom __bottom) (make-array 0 :initial-element 0 :element-type :integer))
    ((:left __left) (make-array 0 :initial-element 0 :element-type :integer))
    ((:right __right) (make-array 0 :initial-element 0 :element-type :integer))
    ((:probability __probability) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _name __name)
   (setq _top __top)
   (setq _bottom __bottom)
   (setq _left __left)
   (setq _right __right)
   (setq _probability __probability)
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:top
   (&optional __top)
   (if __top (setq _top __top)) _top)
  (:bottom
   (&optional __bottom)
   (if __bottom (setq _bottom __bottom)) _bottom)
  (:left
   (&optional __left)
   (if __left (setq _left __left)) _left)
  (:right
   (&optional __right)
   (if __right (setq _right __right)) _right)
  (:probability
   (&optional __probability)
   (if __probability (setq _probability __probability)) _probability)
  (:serialization-length
   ()
   (+
    ;; string[] _name
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _name)) 4
    ;; int32[] _top
    (* 4    (length _top)) 4
    ;; int32[] _bottom
    (* 4    (length _bottom)) 4
    ;; int32[] _left
    (* 4    (length _left)) 4
    ;; int32[] _right
    (* 4    (length _right)) 4
    ;; float64[] _probability
    (* 8    (length _probability)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _name
     (write-long (length _name) s)
     (dolist (elem _name)
       (write-long (length elem) s) (princ elem s)
       )
     ;; int32[] _top
     (write-long (length _top) s)
     (dotimes (i (length _top))
       (write-long (elt _top i) s)
       )
     ;; int32[] _bottom
     (write-long (length _bottom) s)
     (dotimes (i (length _bottom))
       (write-long (elt _bottom i) s)
       )
     ;; int32[] _left
     (write-long (length _left) s)
     (dotimes (i (length _left))
       (write-long (elt _left i) s)
       )
     ;; int32[] _right
     (write-long (length _right) s)
     (dotimes (i (length _right))
       (write-long (elt _right i) s)
       )
     ;; float64[] _probability
     (write-long (length _probability) s)
     (dotimes (i (length _probability))
       (sys::poke (elt _probability i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _name
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _name (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _name i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; int32[] _top
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _top (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _top i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _bottom
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _bottom (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _bottom i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _left
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _left (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _left i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _right
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _right (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _right i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; float64[] _probability
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _probability (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _probability i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get wpb_home_behaviors::Rect :md5sum-) "f2e8cef4f7bbfddf42bb42bcc97ae935")
(setf (get wpb_home_behaviors::Rect :datatype-) "wpb_home_behaviors/Rect")
(setf (get wpb_home_behaviors::Rect :definition-)
      "string[] name
int32[] top
int32[] bottom
int32[] left
int32[] right
float64[] probability
")



(provide :wpb_home_behaviors/Rect "f2e8cef4f7bbfddf42bb42bcc97ae935")


