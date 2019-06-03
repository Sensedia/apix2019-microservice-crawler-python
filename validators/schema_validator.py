from jsonschema import validate as jsonschemavalidator

schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "phone": {
      "type": "string"
    },
    "gender": {
      "type": "string",
      "maxLength": 1
    },
    "specifications": {
      "type": "array",
      "maxItems": 3,  
      "items": [
        {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": ["PANT"]
            },
            "color": {
              "type": "string",
              "enum": ["BLACK", "BLUE", "BROWN", "GREEN", "GREY", "ORANGE", "PINK", "PURPLE", "RED", "WHITE", "YELLOW"]
            }
          },
          "required": [
            "type",
            "color"
          ]
        },
        {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": ["SHIRT"]
            },
            "color": {
              "type": "string",
              "enum": ["BLACK", "BLUE", "BROWN", "GREEN", "GREY", "ORANGE", "PINK", "PURPLE", "RED", "WHITE", "YELLOW"]
            }
          },
          "required": [
            "type",
            "color"
          ]
        },
        {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": ["SHOES"]
            },
            "color": {
              "type": "string",
              "enum": ["BLACK", "BLUE", "BROWN", "GREEN", "GREY", "ORANGE", "PINK", "PURPLE", "RED", "WHITE", "YELLOW"]
            }
          },
          "required": [
            "type",
            "color"
          ]
        }
      ]
    }
  },
  "required": [
    "id",
    "phone",
    "gender",
    "specifications"
  ]
}

def validate(kit):
  try:
      jsonschemavalidator(instance=kit, schema=schema)
      return True
  except Exception as err:
      print('Kit invalido: ' + err.message)
      return False