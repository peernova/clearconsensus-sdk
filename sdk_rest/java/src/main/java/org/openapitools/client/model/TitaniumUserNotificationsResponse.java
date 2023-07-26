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
import org.openapitools.client.model.TitaniumUserNotifications;

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
 * TitaniumUserNotificationsResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-07-26T14:40:43.178538Z[UTC]")
public class TitaniumUserNotificationsResponse {
  public static final String SERIALIZED_NAME_ERROR = "error";
  @SerializedName(SERIALIZED_NAME_ERROR)
  private TitaniumError error;

  public static final String SERIALIZED_NAME_USER_NOTIFICATIONS = "userNotifications";
  @SerializedName(SERIALIZED_NAME_USER_NOTIFICATIONS)
  private TitaniumUserNotifications userNotifications;

  public TitaniumUserNotificationsResponse() { 
  }

  public TitaniumUserNotificationsResponse error(TitaniumError error) {
    
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


  public TitaniumUserNotificationsResponse userNotifications(TitaniumUserNotifications userNotifications) {
    
    this.userNotifications = userNotifications;
    return this;
  }

   /**
   * Get userNotifications
   * @return userNotifications
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumUserNotifications getUserNotifications() {
    return userNotifications;
  }


  public void setUserNotifications(TitaniumUserNotifications userNotifications) {
    this.userNotifications = userNotifications;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumUserNotificationsResponse titaniumUserNotificationsResponse = (TitaniumUserNotificationsResponse) o;
    return Objects.equals(this.error, titaniumUserNotificationsResponse.error) &&
        Objects.equals(this.userNotifications, titaniumUserNotificationsResponse.userNotifications);
  }

  @Override
  public int hashCode() {
    return Objects.hash(error, userNotifications);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumUserNotificationsResponse {\n");
    sb.append("    error: ").append(toIndentedString(error)).append("\n");
    sb.append("    userNotifications: ").append(toIndentedString(userNotifications)).append("\n");
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
    openapiFields.add("userNotifications");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumUserNotificationsResponse
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumUserNotificationsResponse.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumUserNotificationsResponse is not found in the empty JSON string", TitaniumUserNotificationsResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumUserNotificationsResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumUserNotificationsResponse` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      // validate the optional field `error`
      if (jsonObj.getAsJsonObject("error") != null) {
        TitaniumError.validateJsonObject(jsonObj.getAsJsonObject("error"));
      }
      // validate the optional field `userNotifications`
      if (jsonObj.getAsJsonObject("userNotifications") != null) {
        TitaniumUserNotifications.validateJsonObject(jsonObj.getAsJsonObject("userNotifications"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumUserNotificationsResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumUserNotificationsResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumUserNotificationsResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumUserNotificationsResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumUserNotificationsResponse>() {
           @Override
           public void write(JsonWriter out, TitaniumUserNotificationsResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumUserNotificationsResponse read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumUserNotificationsResponse given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumUserNotificationsResponse
  * @throws IOException if the JSON string is invalid with respect to TitaniumUserNotificationsResponse
  */
  public static TitaniumUserNotificationsResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumUserNotificationsResponse.class);
  }

 /**
  * Convert an instance of TitaniumUserNotificationsResponse to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

