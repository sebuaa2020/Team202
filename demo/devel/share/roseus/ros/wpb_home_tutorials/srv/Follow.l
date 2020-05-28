;; Auto-generated. Do not edit!


(when (boundp 'wpb_home_tutorials::Follow)
  (if (not (find-package "WPB_HOME_TUTORIALS"))
    (make-package "WPB_HOME_TUTORIALS"))
  (shadow 'Follow (find-package "WPB_HOME_TUTORIALS")))
(unless (find-package "WPB_HOME_TUTORIALS::FOLLOW")
  (make-package "WPB_HOME_TUTORIALS::FOLLOW"))
(unless (find-package "WPB_HOME_TUTORIALS::FOLLOWREQUEST")
  (make-package "WPB_HOME_TUTORIALS::FOLLOWREQUEST"))
(unless (find-package "WPB_HOME_TUTORIALS::FOLLOWRESPONSE")
  (make-package "WPB_HOME_TUTORIALS::FOLLOWRESPONSE"))

(in-package "ROS")





(defclass wpb_home_tutorials::FollowRequest
  :super ros::object
  :slots (_thredhold ))

(defmethod wpb_home_tutorials::FollowRequest
  (:init
   (&key
    ((:thredhold __thredhold) 0.0)
    )
   (send-super :init)
   (setq _thredhold (float __thredhold))
   self)
  (:thredhold
   (&optional __thredhold)
   (if __thredhold (setq _thredhold __thredhold)) _thredhold)
  (:serialization-length
   ()
   (+
    ;; float32 _thredhold
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _thredhold
       (sys::poke _thredhold (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _thredhold
     (setq _thredhold (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass wpb_home_tutorials::FollowResponse
  :super ros::object
  :slots (_result ))

(defmethod wpb_home_tutorials::FollowResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass wpb_home_tutorials::Follow
  :super ros::object
  :slots ())

(setf (get wpb_home_tutorials::Follow :md5sum-) "24fe904d75d710a2e0b16246fbf996c5")
(setf (get wpb_home_tutorials::Follow :datatype-) "wpb_home_tutorials/Follow")
(setf (get wpb_home_tutorials::Follow :request) wpb_home_tutorials::FollowRequest)
(setf (get wpb_home_tutorials::Follow :response) wpb_home_tutorials::FollowResponse)

(defmethod wpb_home_tutorials::FollowRequest
  (:response () (instance wpb_home_tutorials::FollowResponse :init)))

(setf (get wpb_home_tutorials::FollowRequest :md5sum-) "24fe904d75d710a2e0b16246fbf996c5")
(setf (get wpb_home_tutorials::FollowRequest :datatype-) "wpb_home_tutorials/FollowRequest")
(setf (get wpb_home_tutorials::FollowRequest :definition-)
      "float32 thredhold
---
bool result
")

(setf (get wpb_home_tutorials::FollowResponse :md5sum-) "24fe904d75d710a2e0b16246fbf996c5")
(setf (get wpb_home_tutorials::FollowResponse :datatype-) "wpb_home_tutorials/FollowResponse")
(setf (get wpb_home_tutorials::FollowResponse :definition-)
      "float32 thredhold
---
bool result
")



(provide :wpb_home_tutorials/Follow "24fe904d75d710a2e0b16246fbf996c5")


