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
import org.openapitools.client.model.TitaniumDependency;

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
 * TitaniumColDependency
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T19:18:35.135732Z[UTC]")
public class TitaniumColDependency {
  public static final String SERIALIZED_NAME_COL = "col";
  @SerializedName(SERIALIZED_NAME_COL)
  private String col;

  public static final String SERIALIZED_NAME_DEPENDENCY = "dependency";
  @SerializedName(SERIALIZED_NAME_DEPENDENCY)
  private List<TitaniumDependency> dependency = null;

  public TitaniumColDependency() { 
  }

  public TitaniumColDependency col(String col) {
    
    this.col = col;
    return this;
  }

   /**
   * Get col
   * @return col
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getCol() {
    return col;
  }


  public void setCol(String col) {
    this.col = col;
  }


  public TitaniumColDependency dependency(List<TitaniumDependency> dependency) {
    
    this.dependency = dependency;
    return this;
  }

  public TitaniumColDependency addDependencyItem(TitaniumDependency dependencyItem) {
    if (this.dependency == null) {
      this.dependency = new ArrayList<>();
    }
    this.dependency.add(dependencyItem);
    return this;
  }

   /**
   * Get dependency
   * @return dependency
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumDependency> getDependency() {
    return dependency;
  }


  public void setDependency(List<TitaniumDependency> dependency) {
    this.dependency = dependency;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumColDependency titaniumColDependency = (TitaniumColDependency) o;
    return Objects.equals(this.col, titaniumColDependency.col) &&
        Objects.equals(this.dependency, titaniumColDependency.dependency);
  }

  @Override
  public int hashCode() {
    return Objects.hash(col, dependency);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumColDependency {\n");
    sb.append("    col: ").append(toIndentedString(col)).append("\n");
    sb.append("    dependency: ").append(toIndentedString(dependency)).append("\n");
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
    openapiFields.add("col");
    openapiFields.add("dependency");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumColDependency
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumColDependency.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumColDependency is not found in the empty JSON string", TitaniumColDependency.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumColDependency.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumColDependency` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("col") != null && !jsonObj.get("col").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `col` to be a primitive type in the JSON string but got `%s`", jsonObj.get("col").toString()));
      }
      JsonArray jsonArraydependency = jsonObj.getAsJsonArray("dependency");
      if (jsonArraydependency != null) {
        // ensure the json data is an array
        if (!jsonObj.get("dependency").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `dependency` to be an array in the JSON string but got `%s`", jsonObj.get("dependency").toString()));
        }

        // validate the optional field `dependency` (array)
        for (int i = 0; i < jsonArraydependency.size(); i++) {
          TitaniumDependency.validateJsonObject(jsonArraydependency.get(i).getAsJsonObject());
        };
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumColDependency.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumColDependency' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumColDependency> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumColDependency.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumColDependency>() {
           @Override
           public void write(JsonWriter out, TitaniumColDependency value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumColDependency read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumColDependency given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumColDependency
  * @throws IOException if the JSON string is invalid with respect to TitaniumColDependency
  */
  public static TitaniumColDependency fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumColDependency.class);
  }

 /**
  * Convert an instance of TitaniumColDependency to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

