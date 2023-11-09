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
 * TitaniumUser
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-09T12:07:56.837092Z[UTC]")
public class TitaniumUser {
  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_NOTIFY_BY_APP_ENABLED = "notifyByAppEnabled";
  @SerializedName(SERIALIZED_NAME_NOTIFY_BY_APP_ENABLED)
  private Boolean notifyByAppEnabled;

  public static final String SERIALIZED_NAME_NOTIFY_BY_EMAIL_ENABLED = "notifyByEmailEnabled";
  @SerializedName(SERIALIZED_NAME_NOTIFY_BY_EMAIL_ENABLED)
  private Boolean notifyByEmailEnabled;

  public static final String SERIALIZED_NAME_ORGANIZATION = "organization";
  @SerializedName(SERIALIZED_NAME_ORGANIZATION)
  private String organization;

  public TitaniumUser() { 
  }

  public TitaniumUser email(String email) {
    
    this.email = email;
    return this;
  }

   /**
   * Get email
   * @return email
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getEmail() {
    return email;
  }


  public void setEmail(String email) {
    this.email = email;
  }


  public TitaniumUser id(String id) {
    
    this.id = id;
    return this;
  }

   /**
   * Get id
   * @return id
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getId() {
    return id;
  }


  public void setId(String id) {
    this.id = id;
  }


  public TitaniumUser notifyByAppEnabled(Boolean notifyByAppEnabled) {
    
    this.notifyByAppEnabled = notifyByAppEnabled;
    return this;
  }

   /**
   * Get notifyByAppEnabled
   * @return notifyByAppEnabled
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getNotifyByAppEnabled() {
    return notifyByAppEnabled;
  }


  public void setNotifyByAppEnabled(Boolean notifyByAppEnabled) {
    this.notifyByAppEnabled = notifyByAppEnabled;
  }


  public TitaniumUser notifyByEmailEnabled(Boolean notifyByEmailEnabled) {
    
    this.notifyByEmailEnabled = notifyByEmailEnabled;
    return this;
  }

   /**
   * Get notifyByEmailEnabled
   * @return notifyByEmailEnabled
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getNotifyByEmailEnabled() {
    return notifyByEmailEnabled;
  }


  public void setNotifyByEmailEnabled(Boolean notifyByEmailEnabled) {
    this.notifyByEmailEnabled = notifyByEmailEnabled;
  }


  public TitaniumUser organization(String organization) {
    
    this.organization = organization;
    return this;
  }

   /**
   * Get organization
   * @return organization
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getOrganization() {
    return organization;
  }


  public void setOrganization(String organization) {
    this.organization = organization;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumUser titaniumUser = (TitaniumUser) o;
    return Objects.equals(this.email, titaniumUser.email) &&
        Objects.equals(this.id, titaniumUser.id) &&
        Objects.equals(this.notifyByAppEnabled, titaniumUser.notifyByAppEnabled) &&
        Objects.equals(this.notifyByEmailEnabled, titaniumUser.notifyByEmailEnabled) &&
        Objects.equals(this.organization, titaniumUser.organization);
  }

  @Override
  public int hashCode() {
    return Objects.hash(email, id, notifyByAppEnabled, notifyByEmailEnabled, organization);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumUser {\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    notifyByAppEnabled: ").append(toIndentedString(notifyByAppEnabled)).append("\n");
    sb.append("    notifyByEmailEnabled: ").append(toIndentedString(notifyByEmailEnabled)).append("\n");
    sb.append("    organization: ").append(toIndentedString(organization)).append("\n");
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
    openapiFields.add("email");
    openapiFields.add("id");
    openapiFields.add("notifyByAppEnabled");
    openapiFields.add("notifyByEmailEnabled");
    openapiFields.add("organization");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumUser
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumUser.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumUser is not found in the empty JSON string", TitaniumUser.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumUser.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumUser` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("email") != null && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if (jsonObj.get("id") != null && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (jsonObj.get("organization") != null && !jsonObj.get("organization").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `organization` to be a primitive type in the JSON string but got `%s`", jsonObj.get("organization").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumUser.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumUser' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumUser> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumUser.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumUser>() {
           @Override
           public void write(JsonWriter out, TitaniumUser value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumUser read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumUser given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumUser
  * @throws IOException if the JSON string is invalid with respect to TitaniumUser
  */
  public static TitaniumUser fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumUser.class);
  }

 /**
  * Convert an instance of TitaniumUser to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

