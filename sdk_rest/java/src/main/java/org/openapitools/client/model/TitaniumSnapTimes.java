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
 * TitaniumSnapTimes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-09T09:48:11.178618Z[UTC]")
public class TitaniumSnapTimes {
  public static final String SERIALIZED_NAME_SNAP_TIMES = "snapTimes";
  @SerializedName(SERIALIZED_NAME_SNAP_TIMES)
  private List<String> snapTimes = null;

  public TitaniumSnapTimes() { 
  }

  public TitaniumSnapTimes snapTimes(List<String> snapTimes) {
    
    this.snapTimes = snapTimes;
    return this;
  }

  public TitaniumSnapTimes addSnapTimesItem(String snapTimesItem) {
    if (this.snapTimes == null) {
      this.snapTimes = new ArrayList<>();
    }
    this.snapTimes.add(snapTimesItem);
    return this;
  }

   /**
   * Get snapTimes
   * @return snapTimes
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<String> getSnapTimes() {
    return snapTimes;
  }


  public void setSnapTimes(List<String> snapTimes) {
    this.snapTimes = snapTimes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumSnapTimes titaniumSnapTimes = (TitaniumSnapTimes) o;
    return Objects.equals(this.snapTimes, titaniumSnapTimes.snapTimes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(snapTimes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumSnapTimes {\n");
    sb.append("    snapTimes: ").append(toIndentedString(snapTimes)).append("\n");
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
    openapiFields.add("snapTimes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumSnapTimes
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumSnapTimes.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumSnapTimes is not found in the empty JSON string", TitaniumSnapTimes.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumSnapTimes.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumSnapTimes` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      // ensure the json data is an array
      if (jsonObj.get("snapTimes") != null && !jsonObj.get("snapTimes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `snapTimes` to be an array in the JSON string but got `%s`", jsonObj.get("snapTimes").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumSnapTimes.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumSnapTimes' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumSnapTimes> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumSnapTimes.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumSnapTimes>() {
           @Override
           public void write(JsonWriter out, TitaniumSnapTimes value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumSnapTimes read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumSnapTimes given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumSnapTimes
  * @throws IOException if the JSON string is invalid with respect to TitaniumSnapTimes
  */
  public static TitaniumSnapTimes fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumSnapTimes.class);
  }

 /**
  * Convert an instance of TitaniumSnapTimes to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

