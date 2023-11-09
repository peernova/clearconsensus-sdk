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
import org.openapitools.client.model.TitaniumError;
import org.openapitools.client.model.TitaniumUserNotification;

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
 * TitaniumUserNotificationResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-09T12:10:15.592603Z[UTC]")
public class TitaniumUserNotificationResponse {
  public static final String SERIALIZED_NAME_ERROR = "error";
  @SerializedName(SERIALIZED_NAME_ERROR)
  private TitaniumError error;

  public static final String SERIALIZED_NAME_USER_NOTIFICATION = "userNotification";
  @SerializedName(SERIALIZED_NAME_USER_NOTIFICATION)
  private TitaniumUserNotification userNotification;

  public TitaniumUserNotificationResponse() { 
  }

  public TitaniumUserNotificationResponse error(TitaniumError error) {
    
    this.error = error;
    return this;
  }

   /**
   * Get error
   * @return error
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumError getError() {
    return error;
  }


  public void setError(TitaniumError error) {
    this.error = error;
  }


  public TitaniumUserNotificationResponse userNotification(TitaniumUserNotification userNotification) {
    
    this.userNotification = userNotification;
    return this;
  }

   /**
   * Get userNotification
   * @return userNotification
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumUserNotification getUserNotification() {
    return userNotification;
  }


  public void setUserNotification(TitaniumUserNotification userNotification) {
    this.userNotification = userNotification;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumUserNotificationResponse titaniumUserNotificationResponse = (TitaniumUserNotificationResponse) o;
    return Objects.equals(this.error, titaniumUserNotificationResponse.error) &&
        Objects.equals(this.userNotification, titaniumUserNotificationResponse.userNotification);
  }

  @Override
  public int hashCode() {
    return Objects.hash(error, userNotification);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumUserNotificationResponse {\n");
    sb.append("    error: ").append(toIndentedString(error)).append("\n");
    sb.append("    userNotification: ").append(toIndentedString(userNotification)).append("\n");
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
    openapiFields.add("error");
    openapiFields.add("userNotification");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumUserNotificationResponse
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumUserNotificationResponse.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumUserNotificationResponse is not found in the empty JSON string", TitaniumUserNotificationResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumUserNotificationResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumUserNotificationResponse` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      // validate the optional field `error`
      if (jsonObj.getAsJsonObject("error") != null) {
        TitaniumError.validateJsonObject(jsonObj.getAsJsonObject("error"));
      }
      // validate the optional field `userNotification`
      if (jsonObj.getAsJsonObject("userNotification") != null) {
        TitaniumUserNotification.validateJsonObject(jsonObj.getAsJsonObject("userNotification"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumUserNotificationResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumUserNotificationResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumUserNotificationResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumUserNotificationResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumUserNotificationResponse>() {
           @Override
           public void write(JsonWriter out, TitaniumUserNotificationResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumUserNotificationResponse read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumUserNotificationResponse given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumUserNotificationResponse
  * @throws IOException if the JSON string is invalid with respect to TitaniumUserNotificationResponse
  */
  public static TitaniumUserNotificationResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumUserNotificationResponse.class);
  }

 /**
  * Convert an instance of TitaniumUserNotificationResponse to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

