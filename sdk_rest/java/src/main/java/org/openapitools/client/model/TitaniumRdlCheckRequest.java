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
 * TitaniumRdlCheckRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-07-17T19:07:41.695571Z[UTC]")
public class TitaniumRdlCheckRequest {
  public static final String SERIALIZED_NAME_RDL = "rdl";
  @SerializedName(SERIALIZED_NAME_RDL)
  private String rdl;

  public TitaniumRdlCheckRequest() { 
  }

  public TitaniumRdlCheckRequest rdl(String rdl) {
    
    this.rdl = rdl;
    return this;
  }

   /**
   * Get rdl
   * @return rdl
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getRdl() {
    return rdl;
  }


  public void setRdl(String rdl) {
    this.rdl = rdl;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumRdlCheckRequest titaniumRdlCheckRequest = (TitaniumRdlCheckRequest) o;
    return Objects.equals(this.rdl, titaniumRdlCheckRequest.rdl);
  }

  @Override
  public int hashCode() {
    return Objects.hash(rdl);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumRdlCheckRequest {\n");
    sb.append("    rdl: ").append(toIndentedString(rdl)).append("\n");
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
    openapiFields.add("rdl");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumRdlCheckRequest
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumRdlCheckRequest.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumRdlCheckRequest is not found in the empty JSON string", TitaniumRdlCheckRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumRdlCheckRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumRdlCheckRequest` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("rdl") != null && !jsonObj.get("rdl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rdl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rdl").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumRdlCheckRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumRdlCheckRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumRdlCheckRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumRdlCheckRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumRdlCheckRequest>() {
           @Override
           public void write(JsonWriter out, TitaniumRdlCheckRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumRdlCheckRequest read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumRdlCheckRequest given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumRdlCheckRequest
  * @throws IOException if the JSON string is invalid with respect to TitaniumRdlCheckRequest
  */
  public static TitaniumRdlCheckRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumRdlCheckRequest.class);
  }

 /**
  * Convert an instance of TitaniumRdlCheckRequest to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

