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
 * GetFileExportUrlResponseFileExportUrl
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-09T10:29:00.000800Z[UTC]")
public class GetFileExportUrlResponseFileExportUrl {
  public static final String SERIALIZED_NAME_S3_URL = "s3Url";
  @SerializedName(SERIALIZED_NAME_S3_URL)
  private String s3Url;

  public GetFileExportUrlResponseFileExportUrl() { 
  }

  public GetFileExportUrlResponseFileExportUrl s3Url(String s3Url) {
    
    this.s3Url = s3Url;
    return this;
  }

   /**
   * Get s3Url
   * @return s3Url
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getS3Url() {
    return s3Url;
  }


  public void setS3Url(String s3Url) {
    this.s3Url = s3Url;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetFileExportUrlResponseFileExportUrl getFileExportUrlResponseFileExportUrl = (GetFileExportUrlResponseFileExportUrl) o;
    return Objects.equals(this.s3Url, getFileExportUrlResponseFileExportUrl.s3Url);
  }

  @Override
  public int hashCode() {
    return Objects.hash(s3Url);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetFileExportUrlResponseFileExportUrl {\n");
    sb.append("    s3Url: ").append(toIndentedString(s3Url)).append("\n");
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
    openapiFields.add("s3Url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to GetFileExportUrlResponseFileExportUrl
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (GetFileExportUrlResponseFileExportUrl.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetFileExportUrlResponseFileExportUrl is not found in the empty JSON string", GetFileExportUrlResponseFileExportUrl.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!GetFileExportUrlResponseFileExportUrl.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetFileExportUrlResponseFileExportUrl` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("s3Url") != null && !jsonObj.get("s3Url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `s3Url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("s3Url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetFileExportUrlResponseFileExportUrl.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetFileExportUrlResponseFileExportUrl' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetFileExportUrlResponseFileExportUrl> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetFileExportUrlResponseFileExportUrl.class));

       return (TypeAdapter<T>) new TypeAdapter<GetFileExportUrlResponseFileExportUrl>() {
           @Override
           public void write(JsonWriter out, GetFileExportUrlResponseFileExportUrl value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetFileExportUrlResponseFileExportUrl read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of GetFileExportUrlResponseFileExportUrl given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of GetFileExportUrlResponseFileExportUrl
  * @throws IOException if the JSON string is invalid with respect to GetFileExportUrlResponseFileExportUrl
  */
  public static GetFileExportUrlResponseFileExportUrl fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetFileExportUrlResponseFileExportUrl.class);
  }

 /**
  * Convert an instance of GetFileExportUrlResponseFileExportUrl to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

