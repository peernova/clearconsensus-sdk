/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumErrorDefinition
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T19:08:32.921048Z[UTC]")
public class TitaniumErrorDefinition {
  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_MESSAGE_ARGS = "messageArgs";
  @SerializedName(SERIALIZED_NAME_MESSAGE_ARGS)
  private List<String> messageArgs = null;

  public TitaniumErrorDefinition() { 
  }

  public TitaniumErrorDefinition message(String message) {
    
    this.message = message;
    return this;
  }

   /**
   * Get message
   * @return message
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getMessage() {
    return message;
  }


  public void setMessage(String message) {
    this.message = message;
  }


  public TitaniumErrorDefinition messageArgs(List<String> messageArgs) {
    
    this.messageArgs = messageArgs;
    return this;
  }

  public TitaniumErrorDefinition addMessageArgsItem(String messageArgsItem) {
    if (this.messageArgs == null) {
      this.messageArgs = new ArrayList<>();
    }
    this.messageArgs.add(messageArgsItem);
    return this;
  }

   /**
   * Get messageArgs
   * @return messageArgs
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<String> getMessageArgs() {
    return messageArgs;
  }


  public void setMessageArgs(List<String> messageArgs) {
    this.messageArgs = messageArgs;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumErrorDefinition titaniumErrorDefinition = (TitaniumErrorDefinition) o;
    return Objects.equals(this.message, titaniumErrorDefinition.message) &&
        Objects.equals(this.messageArgs, titaniumErrorDefinition.messageArgs);
  }

  @Override
  public int hashCode() {
    return Objects.hash(message, messageArgs);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumErrorDefinition {\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    messageArgs: ").append(toIndentedString(messageArgs)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("message");
    openapiFields.add("messageArgs");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumErrorDefinition
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumErrorDefinition.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumErrorDefinition is not found in the empty JSON string", TitaniumErrorDefinition.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumErrorDefinition.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumErrorDefinition` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("message") != null && !jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
      // ensure the json data is an array
      if (jsonObj.get("messageArgs") != null && !jsonObj.get("messageArgs").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `messageArgs` to be an array in the JSON string but got `%s`", jsonObj.get("messageArgs").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumErrorDefinition.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumErrorDefinition' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumErrorDefinition> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumErrorDefinition.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumErrorDefinition>() {
           @Override
           public void write(JsonWriter out, TitaniumErrorDefinition value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumErrorDefinition read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumErrorDefinition given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumErrorDefinition
  * @throws IOException if the JSON string is invalid with respect to TitaniumErrorDefinition
  */
  public static TitaniumErrorDefinition fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumErrorDefinition.class);
  }

 /**
  * Convert an instance of TitaniumErrorDefinition to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

