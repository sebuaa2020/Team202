// Auto-generated. Do not edit!

// (in-package wpb_home_tutorials.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class FollowRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.thredhold = null;
    }
    else {
      if (initObj.hasOwnProperty('thredhold')) {
        this.thredhold = initObj.thredhold
      }
      else {
        this.thredhold = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FollowRequest
    // Serialize message field [thredhold]
    bufferOffset = _serializer.float32(obj.thredhold, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FollowRequest
    let len;
    let data = new FollowRequest(null);
    // Deserialize message field [thredhold]
    data.thredhold = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'wpb_home_tutorials/FollowRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c112d3700d2186140dee3c92caad02d8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 thredhold
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FollowRequest(null);
    if (msg.thredhold !== undefined) {
      resolved.thredhold = msg.thredhold;
    }
    else {
      resolved.thredhold = 0.0
    }

    return resolved;
    }
};

class FollowResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.result = null;
    }
    else {
      if (initObj.hasOwnProperty('result')) {
        this.result = initObj.result
      }
      else {
        this.result = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FollowResponse
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FollowResponse
    let len;
    let data = new FollowResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'wpb_home_tutorials/FollowResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'eb13ac1f1354ccecb7941ee8fa2192e8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool result
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FollowResponse(null);
    if (msg.result !== undefined) {
      resolved.result = msg.result;
    }
    else {
      resolved.result = false
    }

    return resolved;
    }
};

module.exports = {
  Request: FollowRequest,
  Response: FollowResponse,
  md5sum() { return '24fe904d75d710a2e0b16246fbf996c5'; },
  datatype() { return 'wpb_home_tutorials/Follow'; }
};
