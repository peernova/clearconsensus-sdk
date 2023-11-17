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
import org.openapitools.client.model.TitaniumColumnInfo;

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
 * TitaniumFields
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T19:41:45.807947Z[UTC]")
public class TitaniumFields {
  public static final String SERIALIZED_NAME_GROUPING_KEYS = "groupingKeys";
  @SerializedName(SERIALIZED_NAME_GROUPING_KEYS)
  private List<TitaniumColumnInfo> groupingKeys = null;

  public TitaniumFields() { 
  }

  public TitaniumFields groupingKeys(List<TitaniumColumnInfo> groupingKeys) {
    
    this.groupingKeys = groupingKeys;
    return this;
  }

  public TitaniumFields addGroupingKeysItem(TitaniumColumnInfo groupingKeysItem) {
    if (this.groupingKeys == null) {
      this.groupingKeys = new ArrayList<>();
    }
    this.groupingKeys.add(groupingKeysItem);
    return this;
  }

   /**
   * Get groupingKeys
   * @return groupingKeys
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumColumnInfo> getGroupingKeys() {
    return groupingKeys;
  }


  public void setGroupingKeys(List<TitaniumColumnInfo> groupingKeys) {
    this.groupingKeys = groupingKeys;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumFields titaniumFields = (TitaniumFields) o;
    return Objects.equals(this.groupingKeys, titaniumFields.groupingKeys);
  }

  @Override
  public int hashCode() {
    return Objects.hash(groupingKeys);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumFields {\n");
    sb.append("    groupingKeys: ").append(toIndentedString(groupingKeys)).append("\n");
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
    openapiFields.add("groupingKeys");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumFields
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumFields.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumFields is not found in the empty JSON string", TitaniumFields.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumFields.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumFields` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      JsonArray jsonArraygroupingKeys = jsonObj.getAsJsonArray("groupingKeys");
      if (jsonArraygroupingKeys != null) {
        // ensure the json data is an array
        if (!jsonObj.get("groupingKeys").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `groupingKeys` to be an array in the JSON string but got `%s`", jsonObj.get("groupingKeys").toString()));
        }

        // validate the optional field `groupingKeys` (array)
        for (int i = 0; i < jsonArraygroupingKeys.size(); i++) {
          TitaniumColumnInfo.validateJsonObject(jsonArraygroupingKeys.get(i).getAsJsonObject());
        };
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumFields.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumFields' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumFields> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumFields.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumFields>() {
           @Override
           public void write(JsonWriter out, TitaniumFields value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumFields read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumFields given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumFields
  * @throws IOException if the JSON string is invalid with respect to TitaniumFields
  */
  public static TitaniumFields fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumFields.class);
  }

 /**
  * Convert an instance of TitaniumFields to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

