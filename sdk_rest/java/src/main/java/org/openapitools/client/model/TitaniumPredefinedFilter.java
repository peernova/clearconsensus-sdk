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
 * TitaniumPredefinedFilter
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-05-10T19:13:00.376912Z[UTC]")
public class TitaniumPredefinedFilter {
  public static final String SERIALIZED_NAME_KEY = "key";
  @SerializedName(SERIALIZED_NAME_KEY)
  private String key;

  public static final String SERIALIZED_NAME_OPERATOR = "operator";
  @SerializedName(SERIALIZED_NAME_OPERATOR)
  private String operator;

  public static final String SERIALIZED_NAME_PREDEFINED_VALUE_LABEL = "predefinedValueLabel";
  @SerializedName(SERIALIZED_NAME_PREDEFINED_VALUE_LABEL)
  private String predefinedValueLabel;

  public static final String SERIALIZED_NAME_RESULT_COUNT = "resultCount";
  @SerializedName(SERIALIZED_NAME_RESULT_COUNT)
  private Integer resultCount;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private Object value;

  public TitaniumPredefinedFilter() { 
  }

  public TitaniumPredefinedFilter key(String key) {
    
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


  public TitaniumPredefinedFilter operator(String operator) {
    
    this.operator = operator;
    return this;
  }

   /**
   * Get operator
   * @return operator
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getOperator() {
    return operator;
  }


  public void setOperator(String operator) {
    this.operator = operator;
  }


  public TitaniumPredefinedFilter predefinedValueLabel(String predefinedValueLabel) {
    
    this.predefinedValueLabel = predefinedValueLabel;
    return this;
  }

   /**
   * Get predefinedValueLabel
   * @return predefinedValueLabel
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getPredefinedValueLabel() {
    return predefinedValueLabel;
  }


  public void setPredefinedValueLabel(String predefinedValueLabel) {
    this.predefinedValueLabel = predefinedValueLabel;
  }


  public TitaniumPredefinedFilter resultCount(Integer resultCount) {
    
    this.resultCount = resultCount;
    return this;
  }

   /**
   * Get resultCount
   * @return resultCount
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getResultCount() {
    return resultCount;
  }


  public void setResultCount(Integer resultCount) {
    this.resultCount = resultCount;
  }


  public TitaniumPredefinedFilter value(Object value) {
    
    this.value = value;
    return this;
  }

   /**
   * Get value
   * @return value
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getValue() {
    return value;
  }


  public void setValue(Object value) {
    this.value = value;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumPredefinedFilter titaniumPredefinedFilter = (TitaniumPredefinedFilter) o;
    return Objects.equals(this.key, titaniumPredefinedFilter.key) &&
        Objects.equals(this.operator, titaniumPredefinedFilter.operator) &&
        Objects.equals(this.predefinedValueLabel, titaniumPredefinedFilter.predefinedValueLabel) &&
        Objects.equals(this.resultCount, titaniumPredefinedFilter.resultCount) &&
        Objects.equals(this.value, titaniumPredefinedFilter.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(key, operator, predefinedValueLabel, resultCount, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumPredefinedFilter {\n");
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    operator: ").append(toIndentedString(operator)).append("\n");
    sb.append("    predefinedValueLabel: ").append(toIndentedString(predefinedValueLabel)).append("\n");
    sb.append("    resultCount: ").append(toIndentedString(resultCount)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
    openapiFields.add("operator");
    openapiFields.add("predefinedValueLabel");
    openapiFields.add("resultCount");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumPredefinedFilter
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumPredefinedFilter.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumPredefinedFilter is not found in the empty JSON string", TitaniumPredefinedFilter.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumPredefinedFilter.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumPredefinedFilter` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("key") != null && !jsonObj.get("key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("key").toString()));
      }
      if (jsonObj.get("operator") != null && !jsonObj.get("operator").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `operator` to be a primitive type in the JSON string but got `%s`", jsonObj.get("operator").toString()));
      }
      if (jsonObj.get("predefinedValueLabel") != null && !jsonObj.get("predefinedValueLabel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `predefinedValueLabel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("predefinedValueLabel").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumPredefinedFilter.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumPredefinedFilter' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumPredefinedFilter> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumPredefinedFilter.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumPredefinedFilter>() {
           @Override
           public void write(JsonWriter out, TitaniumPredefinedFilter value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumPredefinedFilter read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumPredefinedFilter given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumPredefinedFilter
  * @throws IOException if the JSON string is invalid with respect to TitaniumPredefinedFilter
  */
  public static TitaniumPredefinedFilter fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumPredefinedFilter.class);
  }

 /**
  * Convert an instance of TitaniumPredefinedFilter to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

