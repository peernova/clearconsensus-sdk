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
 * TitaniumKVListAsset
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-15T15:17:16.456168Z[UTC]")
public class TitaniumKVListAsset {
  public static final String SERIALIZED_NAME_KEY = "key";
  @SerializedName(SERIALIZED_NAME_KEY)
  private String key;

  public static final String SERIALIZED_NAME_TTL_DATE = "ttlDate";
  @SerializedName(SERIALIZED_NAME_TTL_DATE)
  private String ttlDate;

  public TitaniumKVListAsset() { 
  }

  public TitaniumKVListAsset key(String key) {
    
    this.key = key;
    return this;
  }

   /**
   * Get key
   * @return key
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getKey() {
    return key;
  }


  public void setKey(String key) {
    this.key = key;
  }


  public TitaniumKVListAsset ttlDate(String ttlDate) {
    
    this.ttlDate = ttlDate;
    return this;
  }

   /**
   * Get ttlDate
   * @return ttlDate
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getTtlDate() {
    return ttlDate;
  }


  public void setTtlDate(String ttlDate) {
    this.ttlDate = ttlDate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumKVListAsset titaniumKVListAsset = (TitaniumKVListAsset) o;
    return Objects.equals(this.key, titaniumKVListAsset.key) &&
        Objects.equals(this.ttlDate, titaniumKVListAsset.ttlDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(key, ttlDate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumKVListAsset {\n");
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    ttlDate: ").append(toIndentedString(ttlDate)).append("\n");
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
    openapiFields.add("key");
    openapiFields.add("ttlDate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumKVListAsset
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumKVListAsset.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumKVListAsset is not found in the empty JSON string", TitaniumKVListAsset.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumKVListAsset.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumKVListAsset` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("key") != null && !jsonObj.get("key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("key").toString()));
      }
      if (jsonObj.get("ttlDate") != null && !jsonObj.get("ttlDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ttlDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ttlDate").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumKVListAsset.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumKVListAsset' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumKVListAsset> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumKVListAsset.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumKVListAsset>() {
           @Override
           public void write(JsonWriter out, TitaniumKVListAsset value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumKVListAsset read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumKVListAsset given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumKVListAsset
  * @throws IOException if the JSON string is invalid with respect to TitaniumKVListAsset
  */
  public static TitaniumKVListAsset fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumKVListAsset.class);
  }

 /**
  * Convert an instance of TitaniumKVListAsset to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

