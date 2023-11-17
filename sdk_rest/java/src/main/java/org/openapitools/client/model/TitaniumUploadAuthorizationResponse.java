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
 * TitaniumUploadAuthorizationResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T19:31:55.243371Z[UTC]")
public class TitaniumUploadAuthorizationResponse {
  public static final String SERIALIZED_NAME_IS_VALID = "isValid";
  @SerializedName(SERIALIZED_NAME_IS_VALID)
  private Boolean isValid;

  public static final String SERIALIZED_NAME_TARGET_PATH = "targetPath";
  @SerializedName(SERIALIZED_NAME_TARGET_PATH)
  private String targetPath;

  public static final String SERIALIZED_NAME_UUID = "uuid";
  @SerializedName(SERIALIZED_NAME_UUID)
  private String uuid;

  public TitaniumUploadAuthorizationResponse() { 
  }

  public TitaniumUploadAuthorizationResponse isValid(Boolean isValid) {
    
    this.isValid = isValid;
    return this;
  }

   /**
   * Get isValid
   * @return isValid
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getIsValid() {
    return isValid;
  }


  public void setIsValid(Boolean isValid) {
    this.isValid = isValid;
  }


  public TitaniumUploadAuthorizationResponse targetPath(String targetPath) {
    
    this.targetPath = targetPath;
    return this;
  }

   /**
   * Get targetPath
   * @return targetPath
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getTargetPath() {
    return targetPath;
  }


  public void setTargetPath(String targetPath) {
    this.targetPath = targetPath;
  }


  public TitaniumUploadAuthorizationResponse uuid(String uuid) {
    
    this.uuid = uuid;
    return this;
  }

   /**
   * Get uuid
   * @return uuid
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getUuid() {
    return uuid;
  }


  public void setUuid(String uuid) {
    this.uuid = uuid;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumUploadAuthorizationResponse titaniumUploadAuthorizationResponse = (TitaniumUploadAuthorizationResponse) o;
    return Objects.equals(this.isValid, titaniumUploadAuthorizationResponse.isValid) &&
        Objects.equals(this.targetPath, titaniumUploadAuthorizationResponse.targetPath) &&
        Objects.equals(this.uuid, titaniumUploadAuthorizationResponse.uuid);
  }

  @Override
  public int hashCode() {
    return Objects.hash(isValid, targetPath, uuid);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumUploadAuthorizationResponse {\n");
    sb.append("    isValid: ").append(toIndentedString(isValid)).append("\n");
    sb.append("    targetPath: ").append(toIndentedString(targetPath)).append("\n");
    sb.append("    uuid: ").append(toIndentedString(uuid)).append("\n");
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
    openapiFields.add("isValid");
    openapiFields.add("targetPath");
    openapiFields.add("uuid");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumUploadAuthorizationResponse
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumUploadAuthorizationResponse.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumUploadAuthorizationResponse is not found in the empty JSON string", TitaniumUploadAuthorizationResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumUploadAuthorizationResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumUploadAuthorizationResponse` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("targetPath") != null && !jsonObj.get("targetPath").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `targetPath` to be a primitive type in the JSON string but got `%s`", jsonObj.get("targetPath").toString()));
      }
      if (jsonObj.get("uuid") != null && !jsonObj.get("uuid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uuid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uuid").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumUploadAuthorizationResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumUploadAuthorizationResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumUploadAuthorizationResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumUploadAuthorizationResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumUploadAuthorizationResponse>() {
           @Override
           public void write(JsonWriter out, TitaniumUploadAuthorizationResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumUploadAuthorizationResponse read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumUploadAuthorizationResponse given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumUploadAuthorizationResponse
  * @throws IOException if the JSON string is invalid with respect to TitaniumUploadAuthorizationResponse
  */
  public static TitaniumUploadAuthorizationResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumUploadAuthorizationResponse.class);
  }

 /**
  * Convert an instance of TitaniumUploadAuthorizationResponse to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

