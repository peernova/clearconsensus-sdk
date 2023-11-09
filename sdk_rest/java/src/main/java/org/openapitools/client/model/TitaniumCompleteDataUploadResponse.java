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
 * TitaniumCompleteDataUploadResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-09T09:48:11.178618Z[UTC]")
public class TitaniumCompleteDataUploadResponse {
  public static final String SERIALIZED_NAME_ERROR = "error";
  @SerializedName(SERIALIZED_NAME_ERROR)
  private TitaniumError error;

  public static final String SERIALIZED_NAME_SUCCESS = "success";
  @SerializedName(SERIALIZED_NAME_SUCCESS)
  private Boolean success;

  public TitaniumCompleteDataUploadResponse() { 
  }

  public TitaniumCompleteDataUploadResponse error(TitaniumError error) {
    
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


  public TitaniumCompleteDataUploadResponse success(Boolean success) {
    
    this.success = success;
    return this;
  }

   /**
   * Get success
   * @return success
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getSuccess() {
    return success;
  }


  public void setSuccess(Boolean success) {
    this.success = success;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumCompleteDataUploadResponse titaniumCompleteDataUploadResponse = (TitaniumCompleteDataUploadResponse) o;
    return Objects.equals(this.error, titaniumCompleteDataUploadResponse.error) &&
        Objects.equals(this.success, titaniumCompleteDataUploadResponse.success);
  }

  @Override
  public int hashCode() {
    return Objects.hash(error, success);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumCompleteDataUploadResponse {\n");
    sb.append("    error: ").append(toIndentedString(error)).append("\n");
    sb.append("    success: ").append(toIndentedString(success)).append("\n");
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
    openapiFields.add("success");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumCompleteDataUploadResponse
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumCompleteDataUploadResponse.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumCompleteDataUploadResponse is not found in the empty JSON string", TitaniumCompleteDataUploadResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumCompleteDataUploadResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumCompleteDataUploadResponse` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      // validate the optional field `error`
      if (jsonObj.getAsJsonObject("error") != null) {
        TitaniumError.validateJsonObject(jsonObj.getAsJsonObject("error"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumCompleteDataUploadResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumCompleteDataUploadResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumCompleteDataUploadResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumCompleteDataUploadResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumCompleteDataUploadResponse>() {
           @Override
           public void write(JsonWriter out, TitaniumCompleteDataUploadResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumCompleteDataUploadResponse read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumCompleteDataUploadResponse given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumCompleteDataUploadResponse
  * @throws IOException if the JSON string is invalid with respect to TitaniumCompleteDataUploadResponse
  */
  public static TitaniumCompleteDataUploadResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumCompleteDataUploadResponse.class);
  }

 /**
  * Convert an instance of TitaniumCompleteDataUploadResponse to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

