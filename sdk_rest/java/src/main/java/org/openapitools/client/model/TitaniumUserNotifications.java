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
 * TitaniumUserNotifications
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T19:08:32.921048Z[UTC]")
public class TitaniumUserNotifications {
  public static final String SERIALIZED_NAME_USER_NOTIFICATION = "userNotification";
  @SerializedName(SERIALIZED_NAME_USER_NOTIFICATION)
  private List<TitaniumUserNotification> userNotification = null;

  public TitaniumUserNotifications() { 
  }

  public TitaniumUserNotifications userNotification(List<TitaniumUserNotification> userNotification) {
    
    this.userNotification = userNotification;
    return this;
  }

  public TitaniumUserNotifications addUserNotificationItem(TitaniumUserNotification userNotificationItem) {
    if (this.userNotification == null) {
      this.userNotification = new ArrayList<>();
    }
    this.userNotification.add(userNotificationItem);
    return this;
  }

   /**
   * Get userNotification
   * @return userNotification
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumUserNotification> getUserNotification() {
    return userNotification;
  }


  public void setUserNotification(List<TitaniumUserNotification> userNotification) {
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
    TitaniumUserNotifications titaniumUserNotifications = (TitaniumUserNotifications) o;
    return Objects.equals(this.userNotification, titaniumUserNotifications.userNotification);
  }

  @Override
  public int hashCode() {
    return Objects.hash(userNotification);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumUserNotifications {\n");
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
    openapiFields.add("userNotification");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumUserNotifications
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumUserNotifications.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumUserNotifications is not found in the empty JSON string", TitaniumUserNotifications.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumUserNotifications.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumUserNotifications` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      JsonArray jsonArrayuserNotification = jsonObj.getAsJsonArray("userNotification");
      if (jsonArrayuserNotification != null) {
        // ensure the json data is an array
        if (!jsonObj.get("userNotification").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `userNotification` to be an array in the JSON string but got `%s`", jsonObj.get("userNotification").toString()));
        }

        // validate the optional field `userNotification` (array)
        for (int i = 0; i < jsonArrayuserNotification.size(); i++) {
          TitaniumUserNotification.validateJsonObject(jsonArrayuserNotification.get(i).getAsJsonObject());
        };
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumUserNotifications.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumUserNotifications' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumUserNotifications> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumUserNotifications.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumUserNotifications>() {
           @Override
           public void write(JsonWriter out, TitaniumUserNotifications value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumUserNotifications read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumUserNotifications given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumUserNotifications
  * @throws IOException if the JSON string is invalid with respect to TitaniumUserNotifications
  */
  public static TitaniumUserNotifications fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumUserNotifications.class);
  }

 /**
  * Convert an instance of TitaniumUserNotifications to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

