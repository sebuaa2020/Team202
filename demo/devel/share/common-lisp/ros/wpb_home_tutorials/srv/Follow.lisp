; Auto-generated. Do not edit!


(cl:in-package wpb_home_tutorials-srv)


;//! \htmlinclude Follow-request.msg.html

(cl:defclass <Follow-request> (roslisp-msg-protocol:ros-message)
  ((thredhold
    :reader thredhold
    :initarg :thredhold
    :type cl:float
    :initform 0.0))
)

(cl:defclass Follow-request (<Follow-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Follow-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Follow-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name wpb_home_tutorials-srv:<Follow-request> is deprecated: use wpb_home_tutorials-srv:Follow-request instead.")))

(cl:ensure-generic-function 'thredhold-val :lambda-list '(m))
(cl:defmethod thredhold-val ((m <Follow-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wpb_home_tutorials-srv:thredhold-val is deprecated.  Use wpb_home_tutorials-srv:thredhold instead.")
  (thredhold m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Follow-request>) ostream)
  "Serializes a message object of type '<Follow-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'thredhold))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Follow-request>) istream)
  "Deserializes a message object of type '<Follow-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'thredhold) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Follow-request>)))
  "Returns string type for a service object of type '<Follow-request>"
  "wpb_home_tutorials/FollowRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Follow-request)))
  "Returns string type for a service object of type 'Follow-request"
  "wpb_home_tutorials/FollowRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Follow-request>)))
  "Returns md5sum for a message object of type '<Follow-request>"
  "24fe904d75d710a2e0b16246fbf996c5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Follow-request)))
  "Returns md5sum for a message object of type 'Follow-request"
  "24fe904d75d710a2e0b16246fbf996c5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Follow-request>)))
  "Returns full string definition for message of type '<Follow-request>"
  (cl:format cl:nil "float32 thredhold~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Follow-request)))
  "Returns full string definition for message of type 'Follow-request"
  (cl:format cl:nil "float32 thredhold~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Follow-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Follow-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Follow-request
    (cl:cons ':thredhold (thredhold msg))
))
;//! \htmlinclude Follow-response.msg.html

(cl:defclass <Follow-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Follow-response (<Follow-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Follow-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Follow-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name wpb_home_tutorials-srv:<Follow-response> is deprecated: use wpb_home_tutorials-srv:Follow-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <Follow-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wpb_home_tutorials-srv:result-val is deprecated.  Use wpb_home_tutorials-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Follow-response>) ostream)
  "Serializes a message object of type '<Follow-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Follow-response>) istream)
  "Deserializes a message object of type '<Follow-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Follow-response>)))
  "Returns string type for a service object of type '<Follow-response>"
  "wpb_home_tutorials/FollowResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Follow-response)))
  "Returns string type for a service object of type 'Follow-response"
  "wpb_home_tutorials/FollowResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Follow-response>)))
  "Returns md5sum for a message object of type '<Follow-response>"
  "24fe904d75d710a2e0b16246fbf996c5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Follow-response)))
  "Returns md5sum for a message object of type 'Follow-response"
  "24fe904d75d710a2e0b16246fbf996c5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Follow-response>)))
  "Returns full string definition for message of type '<Follow-response>"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Follow-response)))
  "Returns full string definition for message of type 'Follow-response"
  (cl:format cl:nil "bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Follow-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Follow-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Follow-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Follow)))
  'Follow-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Follow)))
  'Follow-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Follow)))
  "Returns string type for a service object of type '<Follow>"
  "wpb_home_tutorials/Follow")