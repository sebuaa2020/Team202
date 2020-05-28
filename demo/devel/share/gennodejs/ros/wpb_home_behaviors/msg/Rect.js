// Auto-generated. Do not edit!

// (in-package wpb_home_behaviors.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Rect {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.name = null;
      this.top = null;
      this.bottom = null;
      this.left = null;
      this.right = null;
      this.probability = null;
    }
    else {
      if (initObj.hasOwnProperty('name')) {
        this.name = initObj.name
      }
      else {
        this.name = [];
      }
      if (initObj.hasOwnProperty('top')) {
        this.top = initObj.top
      }
      else {
        this.top = [];
      }
      if (initObj.hasOwnProperty('bottom')) {
        this.bottom = initObj.bottom
      }
      else {
        this.bottom = [];
      }
      if (initObj.hasOwnProperty('left')) {
        this.left = initObj.left
      }
      else {
        this.left = [];
      }
      if (initObj.hasOwnProperty('right')) {
        this.right = initObj.right
      }
      else {
        this.right = [];
      }
      if (initObj.hasOwnProperty('probability')) {
        this.probability = initObj.probability
      }
      else {
        this.probability = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Rect
    // Serialize message field [name]
    bufferOffset = _arraySerializer.string(obj.name, buffer, bufferOffset, null);
    // Serialize message field [top]
    bufferOffset = _arraySerializer.int32(obj.top, buffer, bufferOffset, null);
    // Serialize message field [bottom]
    bufferOffset = _arraySerializer.int32(obj.bottom, buffer, bufferOffset, null);
    // Serialize message field [left]
    bufferOffset = _arraySerializer.int32(obj.left, buffer, bufferOffset, null);
    // Serialize message field [right]
    bufferOffset = _arraySerializer.int32(obj.right, buffer, bufferOffset, null);
    // Serialize message field [probability]
    bufferOffset = _arraySerializer.float64(obj.probability, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Rect
    let len;
    let data = new Rect(null);
    // Deserialize message field [name]
    data.name = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [top]
    data.top = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [bottom]
    data.bottom = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [left]
    data.left = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [right]
    data.right = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [probability]
    data.probability = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.name.forEach((val) => {
      length += 4 + val.length;
    });
    length += 4 * object.top.length;
    length += 4 * object.bottom.length;
    length += 4 * object.left.length;
    length += 4 * object.right.length;
    length += 8 * object.probability.length;
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'wpb_home_behaviors/Rect';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f2e8cef4f7bbfddf42bb42bcc97ae935';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] name
    int32[] top
    int32[] bottom
    int32[] left
    int32[] right
    float64[] probability
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Rect(null);
    if (msg.name !== undefined) {
      resolved.name = msg.name;
    }
    else {
      resolved.name = []
    }

    if (msg.top !== undefined) {
      resolved.top = msg.top;
    }
    else {
      resolved.top = []
    }

    if (msg.bottom !== undefined) {
      resolved.bottom = msg.bottom;
    }
    else {
      resolved.bottom = []
    }

    if (msg.left !== undefined) {
      resolved.left = msg.left;
    }
    else {
      resolved.left = []
    }

    if (msg.right !== undefined) {
      resolved.right = msg.right;
    }
    else {
      resolved.right = []
    }

    if (msg.probability !== undefined) {
      resolved.probability = msg.probability;
    }
    else {
      resolved.probability = []
    }

    return resolved;
    }
};

module.exports = Rect;
